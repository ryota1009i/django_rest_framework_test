from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry, Comment
from .serializer import UserSerializer, EntrySerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('author', 'status')

class ComnnetViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def index(request):
    entries = Entry.objects.order_by('-id')
    return render(request, 'index.html', {'entries': entries})
