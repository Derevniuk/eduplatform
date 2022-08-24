from django.urls import path
from .endpoints import (
    UserListAPIView,
    UserDetailApi,
    TeacherListAPIView,
    TeacherDetailApi,
    StudentListAPIView,
    StudentDetailApi,
    GroupListAPIView,
    GroupDetailApi)

urlpatterns = [
    path('users/',UserListAPIView.as_view()),
    path('users/<int:pk>',UserDetailApi.as_view()),
    path('users/teachers/',TeacherListAPIView.as_view()),
    path('users/teachers/<int:pk>',TeacherDetailApi.as_view()),
    path('users/students/',StudentListAPIView.as_view()),
    path('users/students/<int:pk>',StudentDetailApi.as_view()),
    path('users/groups/',GroupListAPIView.as_view()),
    path('users/groups/<int:pk>',GroupDetailApi.as_view()),
]
