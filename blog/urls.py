from rest_framework import routers
from .views import UserViewSet, EntryViewSet, ComnnetViewSet
from django.urls import path
from . import views

api_router = routers.DefaultRouter()
api_router.register(r'users', UserViewSet)
api_router.register(r'entries', EntryViewSet)
api_router.register(r'comments', ComnnetViewSet)

urlpatterns = [
    path(r'', views.index, name='index')
]