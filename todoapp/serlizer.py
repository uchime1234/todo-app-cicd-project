from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TodoItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TodoItemSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'description', 'status', 
                 'created_by', 'created_at', 'updated_at', 'due_date']
        read_only_fields = ['created_by', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        # Set the created_by user from request
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)