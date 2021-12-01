from django.urls import path
from rest_framework import routers

from .views import TodoAPIView, TodosAPIView, DoneTodoAPIView, DoneTodosAPIView
# from .views import TodoViewSet

# router = routers.SimpleRouter()
# router.register('todo', TodoViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
    path('todo/<int:pk>/', TodoAPIView.as_view()),
    path('done/', DoneTodosAPIView.as_view()),
    path('done/<int:pk>/', DoneTodoAPIView.as_view()),
]
