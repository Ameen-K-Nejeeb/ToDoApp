from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='list'),
    path('update_task/<pk>/',views.updateTask,name='update_task'),
    path('delete/<pk>/',views.deleteTask,name='delete'),
]
