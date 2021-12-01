from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer, TodoCreateSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()

    # serializer_class = TodoSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return TodoCreateSerializer
        return TodoSerializer