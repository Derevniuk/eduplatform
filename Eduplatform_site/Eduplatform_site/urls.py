from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_account/", include("account.urls"), name="api_account"),
    path("api_learning/", include("learning.urls"), name="api_learning"),
]
