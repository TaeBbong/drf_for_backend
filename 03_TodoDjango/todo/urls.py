from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>', views.todo_detail, name='todo_detail'),
    path('todo', views.todo_post, name='todo_post'),
]
