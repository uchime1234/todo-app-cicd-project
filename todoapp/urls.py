# todoapp/urls.py (APP LEVEL)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # ← IMPORTANT: imports from same app

router = DefaultRouter()
router.register(r'todos', views.TodoItemViewSet, basename='todo')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]