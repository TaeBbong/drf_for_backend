from django.urls import path
from rest_framework import routers

from .views import TodoViewSet

router = routers.SimpleRouter()
router.register('todo', TodoViewSet)

urlpatterns = router.urls
