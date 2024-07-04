from django.shortcuts import render

from .models import AbsenceRequest
from rest_framework import generics

from .serializers import AbsenceSerializerAll

# Create your views here.

# GET the requests of ALL users
class AbsenceGetAll(generics.ListAPIView):
    """
    Retrieve the absence requests for all users
    """
    queryset = AbsenceRequest.objects.all()
    serializer_class = AbsenceSerializerAll
