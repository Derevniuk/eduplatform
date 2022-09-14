from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    GroupTeacherViewAPI,
    GroupViewSet,
    StudentViewSet,
    TeacherViewSet,
    UserViewSet,
    RegisterViewApi,
    LoginViewApi,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"students", StudentViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"groups", GroupViewSet)


urlpatterns = [
    path("", include(router.urls)),
    re_path(
        "teachers/(?P<id>.+)/group",
        GroupTeacherViewAPI.as_view(),
        name="teacher_groups",
    ),
    path('register/',RegisterViewApi.as_view({'get': 'list_user','post':'create'}),name = 'create_user'),
    path('login/',LoginViewApi.as_view(), name = 'login_user'),
]
