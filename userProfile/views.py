from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserProfile
from rest_framework import generics, status

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
    List all UserProfiles where the logged-in user is approver of
    """
    serializer_class = UserProfileSerializerAll
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserProfile.objects.filter(approver__customUser=user)


class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializerAll
    lookup_field = 'customUser__username'

    def get(self, request, *args, **kwargs):
        user_profile = self.get_object()
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)