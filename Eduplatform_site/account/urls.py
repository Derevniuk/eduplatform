from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .endpoints import UserViewSet, StudentViewSet, GroupViewSet, TeacherViewSet, GroupTeacherViewAPI

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'students',StudentViewSet)
router.register(r'teachers',TeacherViewSet)
router.register(r'groups',GroupViewSet)


urlpatterns = [
    path('',include(router.urls)),
    re_path("teachers/(?P<id>.+)/group", GroupTeacherViewAPI.as_view(), name="teacher_groups"),
]