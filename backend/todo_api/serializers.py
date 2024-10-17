from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ['task', 'completed', 'user', 'created_at', 'updated_at']