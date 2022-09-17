from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .endpoints import (
    GroupTeacherViewAPI,
    GroupViewSet,
    RegisterViewApi,
    StudentViewSet,
    TeacherViewSet,
    UserViewSet,
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
    path("register/", RegisterViewApi.as_view({"get": "list_user", "post": "create"}), name="create_user"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
