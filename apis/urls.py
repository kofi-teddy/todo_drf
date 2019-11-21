from django.urls import path

from .views import ListTodo, DetailTodo, TodoViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', ListTodo.as_view()),
#     path('/<int:pk>/', DetailTodo.as_view()),
# ]

router = DefaultRouter()
router.register('', TodoViewSet, base_name='todos')
urlpatterns = router.urls
