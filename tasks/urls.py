from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
]