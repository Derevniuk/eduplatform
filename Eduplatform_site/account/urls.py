from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .endpoints import UserViewSet, StudentViewSet, GroupViewSet, PhotoViewSet,TeacherViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'students',StudentViewSet)
router.register(r'teachers',TeacherViewSet)
router.register(r'groups',GroupViewSet)
router.register(r'photos',PhotoViewSet)


urlpatterns = [
    path('',include(router.urls)),
    # path('teachers/',TeacherViewSet.as_view())
]
# from .endpoints import (
#     UserListAPIView,
#     UserDetailApi,
#     TeacherListAPIView,
#     TeacherDetailApi,
#     StudentListAPIView,
#     StudentDetailApi,
#     GroupListAPIView,
#     GroupDetailApi)
#
# urlpatterns = [
#     path('users/',UserListAPIView.as_view()),
#     path('users/<int:pk>',UserDetailApi.as_view()),
#     path('users/teachers/',TeacherListAPIView.as_view()),
#     path('users/teachers/<int:pk>',TeacherDetailApi.as_view()),
#     path('users/students/',StudentListAPIView.as_view()),
#     path('users/students/<int:pk>',StudentDetailApi.as_view()),
#     path('users/groups/',GroupListAPIView.as_view()),
#     path('users/groups/<int:pk>',GroupDetailApi.as_view()),
# ]
