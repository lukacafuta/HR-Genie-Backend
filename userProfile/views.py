from django.shortcuts import render

from .models import UserProfile
from rest_framework import generics

from .serializers import UserProfileSerializerAll

# Create your views here.

#GET the list of ALL users
#class UserProfileGetAll(generics.RetrieveAPIView):
    #lookup_field = 'pk'

class UserProfileGetAll(generics.ListAPIView):
#class UserProfileGetAll(generics.ListCreateAPIView):
    """
    Retrieve the list of ALL UserProfiles
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializerAll

