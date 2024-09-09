from rest_framework import serializers
from todolist.models import Task  # Assure-toi que le chemin d'importation est correct

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'due_date', 'status']  # Choisis les champs que tu veux exposer via l'API
