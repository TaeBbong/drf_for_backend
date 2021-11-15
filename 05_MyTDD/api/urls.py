from django.urls import path
from .views import CreateView

urlpatterns = [
    path('books/', CreateView.as_view()),
]
