from django.urls import path

from todolist import views



urlpatterns = [
    path('todolist', views.task_list, name='task_list'),
    path('todolist/add/', views.task_add, name='task_add'),
    path('todolist/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('todolist/<int:pk>/delete/', views.task_delete, name='task_delete'),

]
