from django.contrib import admin
from django.urls import include, path
from apis import views

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/v1/', include('apis.urls')),
]

