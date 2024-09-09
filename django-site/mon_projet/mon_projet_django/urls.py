from django.contrib import admin
from django.urls import path, include
from todolist import views as todolist_views
from rest_framework.routers import DefaultRouter
from api import views as api_views

# Création d'un routeur et enregistrement de nos viewsets
router = DefaultRouter()
router.register(r'tasks', api_views.TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', todolist_views.task_list, name='task_list'),
    path('todolist/add/', todolist_views.task_add, name='task_add'),
    path('todolist/<int:pk>/edit/', todolist_views.task_edit, name='task_edit'),
    path('todolist/<int:pk>/delete/', todolist_views.task_delete, name='task_delete'),
    path('api/', include(router.urls)),  # Utilise le routeur pour les URLs de l'API
]
