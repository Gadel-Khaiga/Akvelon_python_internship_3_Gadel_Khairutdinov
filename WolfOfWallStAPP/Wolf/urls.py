from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('create/', WolfCreateView.as_view()),          #create a record in the database
    path('all/', WolfListView.as_view()),               #see all entries
    path('detail/<int:pk>/', WolfDetailView.as_view()), #see user data by id (1,2,3 ....)
]
