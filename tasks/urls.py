from django.urls import path
from .views import *


urlpatterns = [
    path('add_task/', TaskList.as_view()),
    path('testing1/', Testing1.as_view()),
    path('testing2/', Testing2.as_view()),
    path('testing3/', Testing3.as_view()),
    path('task_list/', TaskList.as_view()),
    path('fetch_tasks/', TasksView.as_view()),
    path('edit_task/<int:pk>/', TaskList.as_view()),
    path('get_task/<str:title>/', getTask.as_view()),
    path('delete_task/<int:pk>/', TaskList.as_view()),
    path('message_api/', messageAPI.as_view()),
]
