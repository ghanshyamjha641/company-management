from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("usermanagement/", include("UserManagement.urls")),
    path("admin/", admin.site.urls),
]