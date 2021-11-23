from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>', views.todo_detail, name='todo_detail'),
    path('todo', views.todo_post, name='todo_post'),
    path('done', views.done_list, name='done_list'),
    path('todo/<int:pk>/done', views.todo_done, name='todo_done'),
    path('todo/<int:pk>/edit', views.todo_edit, name='todo_edit'),
]
