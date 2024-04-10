from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('todo', views.todo, name='todo'),
    path('update_todo/<int:id>/', views.update_todo, name= 'update_todo'),
    path('delete_todo/<int:id>/', views.delete_todo, name= 'delete_todo'),
]