from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .endpoints import (
    RegisterViewApi,
    UserViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)



urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterViewApi.as_view({"get": "list_user", "post": "create"}), name="create_user"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
