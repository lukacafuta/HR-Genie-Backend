from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

# import models
from .models import AbsenceRequest
from userProfile.models import UserProfile
#from customUser import CustomUser  # to filter id

# serializers
from .serializers import AbsenceSerializerAll

# Create your views here.

# ..........................................................
# GET the requests of ALL users
class AbsenceGetAll(ListAPIView):
    """
    Retrieve the absence requests for all users
    """
    queryset = AbsenceRequest.objects.all()
    serializer_class = AbsenceSerializerAll


# .............................................................
class CreateListModifyAbsenceMeView(GenericAPIView):
    """
    Absences of the logged-in user: Retrieve the list, patch some, post a new one
    """

    # variables needed in more than 1 function: does it work?
    #id_CustomUserHere = self.request.user.id
    #id_userProfileGlobal = 0

    # define serializer for special cases
    def get_serializer_class(self):
        # if self.request.method == 'GET':
        #    return CustomUserSerializerPrivate  # private info
        # return CustomUserSerializerPublic  # PATCH -> only public patch according to the specifics
        return AbsenceSerializerAll  # simple by now


    # filter the logged-in user via the CustomUser table
    def get_queryset(self):
        # I want the entries of userProfile whose customUser_id = id of the CustomUser
        # get id of CustomUser where username=self.request.user
        id_CustomUserHere = self.request.user.id

        # get the id in UserProfile with this customUser_id
        id_UserProfileHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id

        # save in global var: does it work?
        #global id_userProfileGlobal
        #super.id_userProfileGlobal = id_UserProfileHere

        #pass

        # return the entries of the AbsenceRequest whose requester_id is = this above
        return AbsenceRequest.objects.filter(requester_id=id_UserProfileHere)
        # return UserProfile.objects.all()  # test

    # GET method
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)  # need to put many=True for it to work: boh
        # serializer_class = UserProfileSerializerAll # with this it does not work
        return Response(serializer.data)  # here it sees no data


    # Post a new absence for me only
    def post(self, request, *args, **kwargs):
        # I want the entries of userProfile whose customUser_id = id of the CustomUser
        # get id of CustomUser where username=self.request.user
        id_CustomUserHere = self.request.user.id

        # get the id in UserProfile with this customUser_id
        id_UserProfileHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id

        # get the data passed
        serializer = self.get_serializer(data=request.data)
        # check the data
        serializer.is_valid(raise_exception=True)
        # do such that the requester id is the logged in user of UserProfile
        serializer.save(requester_id=id_UserProfileHere)  #
        return Response(serializer.data, status=status.HTTP_201_CREATED)
