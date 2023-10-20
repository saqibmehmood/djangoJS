from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
import requests
import json
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5  # Number of tasks to display per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Maximum page size allowed

class TasksView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomPagination


import logging

logger = logging.getLogger(__name__)


class Testing1(APIView):
    def get(self, request):
        try:
            print("I am working at this point")
            # response = requests.get(url= "http://127.0.0.1:8000/api/tasks/testing2/")
            response = requests.get(url="http://web:8000/api/tasks/testing2/")
            # if len(json.loads(response.text)['data']) == 0:
            #     return json.loads(response.text)

            print("got raw measurements")
            response = json.loads(response.content.decode())
            return Response({"message": response['message']}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class Testing2(APIView):
    def get(self, request):
        message = "I am from test 2"
        generate_csv(request)
        return Response({"message": message}, status=status.HTTP_201_CREATED)


from django.http import HttpResponse
import csv
import os

def generate_csv(request):
    # Create a list of sample data
    data = [
        ['Name', 'Age'],
        ['John', '30'],
        ['Jane', '25'],
    ]

    # Determine the path for the CSV file within the container
    csv_file_path = '/app/media/data.csv'  # Assuming /app exists in the container

    # Create a CSV file and write data to it
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

    # Return the CSV file as a download
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    response.write(open(csv_file_path, 'rb').read())

    return response
class TaskList(APIView):
    # permission_classes = [IsAuthenticated]
    """
    List all tasks or create a new task.
    """
    pagination_class = CustomPagination

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, format=None):
        tasks = Task.objects.all()

        # Use the pagination_class for pagination
        paginator = self.pagination_class()
        paginated_tasks = paginator.paginate_queryset(tasks, request, view=self)

        serializer = TaskSerializer(paginated_tasks, many=True)
        return paginator.get_paginated_response(serializer.data)


    def post(self, request, format=None):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            task = self.get_object(pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class getTask(APIView):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class messageAPI(APIView):
    def post(self, request):
        try:
            if request.data['option'] == int(1):
                return Response({'message': "you choosed option 1"}, status=status.HTTP_200_OK)
            else:
                return Response({'message': "you choosed option some other option"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

