from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Add a custom message to the response
        representation['message'] = 'Your task has added succesfully :)'

        return representation
