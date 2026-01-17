from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import TodoItem
from .serlizer import TodoItemSerializer, UserSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see their own todos
        return TodoItem.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        todo = self.get_object()
        todo.status = 'completed'
        todo.save()
        return Response({'status': 'todo completed'})
    
    @action(detail=False)
    def stats(self, request):
        todos = self.get_queryset()
        return Response({
            'total': todos.count(),
            'completed': todos.filter(status='completed').count(),
            'pending': todos.filter(status='pending').count(),
            'in_progress': todos.filter(status='in_progress').count(),
        })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer