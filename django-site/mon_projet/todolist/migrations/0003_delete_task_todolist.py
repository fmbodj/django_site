# Generated by Django 5.1.1 on 2024-09-06 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_task_todolist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='task_todolist',
        ),
    ]
