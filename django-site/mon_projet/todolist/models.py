from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.BooleanField(default=False)  # False = not done, True = done

    def __str__(self):
        return self.title
class task_todolist(models.Model):
    title = models.CharField(max_length=255)