from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer, TodoCreateSerializer


class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = get_object_or_404(id=pk)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoneTodosAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoneTodoAPIView(APIView):
    def get(self, request, pk):
        done = get_object_or_404(Todo, id=pk)
        done.complete = True
        done.save()
        serializer = TodoSerializer(done)
        return Response(status=status.HTTP_200_OK)


# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()

#     # serializer_class = TodoSerializer

#     def get_serializer_class(self):
#         if self.action == 'create':
#             return TodoCreateSerializer
#         return TodoSerializer