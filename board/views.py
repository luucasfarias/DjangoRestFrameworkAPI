from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_frameworker import authentication, permissions, viewsets
from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer

User = get_user_model()


class DefaultMixin(object):
    """Configurações default para autenticação e permissão,
    filtragem e paginação da view."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.isAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class SprintViewSet(DefaultMixin, viewsets.ModelViewSet):
    """Endpoint da API para criar e listar as sprints"""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer


class TaskViewSet(DefaultMixin, viewsets.ModelViewSet):
    """Endepoint da API para listar e criar as tarefas."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):
    """Endepoint da API para listar usuarios."""
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
