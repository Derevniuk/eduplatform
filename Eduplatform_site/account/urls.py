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
]
