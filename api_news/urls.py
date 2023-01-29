from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import APITypeViewSet, APINewsViewSet

router = DefaultRouter()
router.register('types', APITypeViewSet)
router.register('news', APINewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]