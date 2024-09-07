from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description',  'due_date', 'status']  # Adapte cette liste selon les champs de ton modèle
