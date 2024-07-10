from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

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


class UserProfileByApproverView(generics.ListAPIView):
    """
    Retrieve the list of all UserProfiles where the logged-in user is approver
    """
    serializer_class = UserProfileSerializerAll
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserProfile.objects.filter(approver__customUser=user)

