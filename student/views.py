from django.shortcuts import render

from rest_framework import viewsets

from .serializers import studentSerializer
from .models import student


class studentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all().order_by('first_name')
    serializer_class = studentSerializer