from django.urls import path
from .views import *

urlpatterns = [
    path('list/', SchoolList.as_view(), name='school_list')
]