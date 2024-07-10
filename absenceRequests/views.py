from django.db.models import Subquery
from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

# import models
from .models import AbsenceRequest
from userProfile.models import UserProfile
#from customUser import CustomUser  # to filter id

# serializers
from .serializers import AbsenceSerializerAll, AbsenceSerializerManager

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
        Retrieve the list of all absence requests of the logged-in user (employee or manager)
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
        """
            Creates a new absence request for the logged-in employee.

           The requester_id is set automatically as the logged-in user.

            Possible reason:
                - vacation (default if not specified)
                - sick_leave

            The status gets set automatically:
                - if reason = sick_leave, then status = 'accepted'
                - other reasons -> status = 'pending'

            Validations performed:
                - checked that startDt < endDt
        """
        # I want the entries of userProfile whose customUser_id = id of the CustomUser
        # get id of CustomUser where username=self.request.user
        id_CustomUserHere = self.request.user.id

        # get the id in UserProfile with this customUser_id
        id_UserProfileHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id

        # get the data passed
        serializer = self.get_serializer(data=request.data)
        # check the data
        serializer.is_valid(raise_exception=True)

        #pass

        # put status = accepted if sick_leave, else pending
        # I need to put it here and not in the serializer bc the status does not get pushed
        # handle the case of reason not specified -> it is vacation
        try:
            if serializer.validated_data['reason'] in ['sick_leave']:
                status_here = 'accepted'
            else:
                status_here = 'pending'
        except:
            # if here -> reason is not specified -> it is vacation
            status_here = 'pending'

        #pass

        # do such that the requester id is the logged in user of UserProfile
        serializer.save(requester_id=id_UserProfileHere, status=status_here)

        #pass

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# .............................................................
class CreateListModifyAbsenceEmployeeMyTeamView(GenericAPIView):
    """
        Retrieve the list of all absence requests of all the users with the same approver as the logged-in person.
        The logged in person is included in the query.
        This is to be used when the logged in user is an employee.

        Next:
        - one endpoint for the manager: his team, his employees, his approver and the people with the same approver
    """
    pass

    # define serializer for special cases
    def get_serializer_class(self):
        # if self.request.method == 'GET':
        #    return CustomUserSerializerPrivate  # private info
        # return CustomUserSerializerPublic  # PATCH -> only public patch according to the specifics
        return AbsenceSerializerAll  # simple by now


    # filter the logged-in user via the CustomUser table
    # and extract the users with the same approver and add the approver
    def get_queryset(self):
        # I want the entries of userProfile whose customUser_id = id of the CustomUser
        # get id of CustomUser where username=self.request.user
        id_CustomUserHere = self.request.user.id

        # get the id in UserProfile with this customUser_id
        id_UserProfileHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id

        # SQL I NEED -> solved with subqueries
        """
         SELECT abs.* FROM AbsenceRequests as abs
         LEFT JOIN
         UserProfile as user
         ON abs.requester_id IN (
            SELECT us2.id
            FROM UserProfile as us2
            WHERE us2.approver_id = fixed value        
         )
        
        """

        # the userProfile id of the approver
        id_approverHere = UserProfile.objects.get(id=id_UserProfileHere).approver_id

        # USING THIS to study: https://docs.djangoproject.com/en/5.0/topics/db/queries/
        # Methods of the queryset = https://docs.djangoproject.com/en/5.0/ref/models/querysets/

        # Subquery to get related_field values from RelatedModel
        # take the list of UserProfile id with the same approver as the logged in user -> it is a list
        subquery = UserProfile.objects.filter(approver=id_approverHere).values('id')

        # Filter MyModel using the subquery
        # return the list of absence request with this filter
        return AbsenceRequest.objects.filter(requester__in=Subquery(subquery))



    # GET method
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)  # need to put many=True for it to work: boh
        # serializer_class = UserProfileSerializerAll # with this it does not work
        return Response(serializer.data)  # here it sees no data


# .............................................................
class CreateListModifyAbsenceEmployeeMyManagerView(GenericAPIView):
    """
        Retrieve the list of all absence requests of the approver of the logged-in user.
        This is for the employees.
    """

    # define serializer for special cases
    def get_serializer_class(self):
        # if self.request.method == 'GET':
        #    return CustomUserSerializerPrivate  # private info
        # return CustomUserSerializerPublic  # PATCH -> only public patch according to the specifics
        return AbsenceSerializerAll  # simple by now

    # filter the logged-in user via the CustomUser table
    # and extract the users with the same approver and add the approver
    def get_queryset(self):
        # I want the entries of userProfile whose customUser_id = id of the CustomUser
        # get id of CustomUser where username=self.request.user
        id_CustomUserHere = self.request.user.id

        # get the id in UserProfile with this customUser_id
        id_UserProfileHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id

        # SQL I NEED -> solved with subqueries


        # the userProfile id of the approver
        id_approverHere = UserProfile.objects.get(id=id_UserProfileHere).approver_id

        # USING THIS to study: https://docs.djangoproject.com/en/5.0/topics/db/queries/
        # Methods of the queryset = https://docs.djangoproject.com/en/5.0/ref/models/querysets/

        # Subquery to get related_field values from RelatedModel
        # take the list of UserProfile id with the same approver as the logged in user -> it is a list
        subquery = UserProfile.objects.filter(id=id_approverHere).values('id')

        # Filter MyModel using the subquery
        # return the list of absence request with this filter
        return AbsenceRequest.objects.filter(requester__in=Subquery(subquery))

    # GET method
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)  # need to put many=True for it to work: boh
        # serializer_class = UserProfileSerializerAll # with this it does not work
        return Response(serializer.data)  # here it sees no data


# .............................................................
class ListAbsenceManagerMyTeamView(GenericAPIView):
    """
        Retrieve the list of all absence requests of all the users whose approver is the logged-in user.
        The logged in person is excluded by this query.
    """


    # define serializer for special cases
    def get_serializer_class(self):
        # if self.request.method == 'GET':
        #    return CustomUserSerializerPrivate  # private info
        # return CustomUserSerializerPublic  # PATCH -> only public patch according to the specifics
        return AbsenceSerializerAll  # simple by now

    # filter the logged-in user via the CustomUser table
    # and extract the users with the same approver and add the approver
    def get_queryset(self):
        # I want the entries of userProfile whose customUser_id = id of the CustomUser
        # get id of CustomUser where username=self.request.user
        id_CustomUserHere = self.request.user.id

        # get the id in UserProfile with this customUser_id
        # the id of the manager is the id of the approver
        #id_UserProfileHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id
        id_approverHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id

        # the userProfile id of the approver
        #id_approverHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).approver_id

        # USING THIS to study: https://docs.djangoproject.com/en/5.0/topics/db/queries/
        # Methods of the queryset = https://docs.djangoproject.com/en/5.0/ref/models/querysets/

        # Subquery to get related_field values from RelatedModel
        # take the list of UserProfile id with the same approver as the logged in user -> it is a list
        subquery = UserProfile.objects.filter(approver=id_approverHere).values('id')

        # Filter MyModel using the subquery
        # return the list of absence request with this filter
        return AbsenceRequest.objects.filter(requester__in=Subquery(subquery))

    # GET method
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)  # need to put many=True for it to work: boh
        # serializer_class = UserProfileSerializerAll # with this it does not work
        return Response(serializer.data)  # here it sees no data

# .............................................................
class ModifyAbsenceManagerMyTeamView(GenericAPIView):
    """
        Retrieve the list of all absence requests of all the users whose approver is the logged-in user.
        The logged in person is excluded by this query.
    """

    # define serializer for special cases
    def get_serializer_class(self):
        # if self.request.method == 'GET':
        #    return CustomUserSerializerPrivate  # private info
        # return CustomUserSerializerPublic  # PATCH -> only public patch according to the specifics
        #return AbsenceSerializerAll  # simple by now
        return AbsenceSerializerManager
        # we use a different serializer for the patch



    # do I need this???
    def get_queryset(self):
        # I want the entries of userProfile whose customUser_id = id of the CustomUser
        # get id of CustomUser where username=self.request.user
        id_CustomUserHere = self.request.user.id

        # get the id in UserProfile with this customUser_id
        # the id of the manager is the id of the approver
        #id_UserProfileHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id
        id_approverHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).id

        # the userProfile id of the approver
        #id_approverHere = UserProfile.objects.get(customUser_id=id_CustomUserHere).approver_id

        # USING THIS to study: https://docs.djangoproject.com/en/5.0/topics/db/queries/
        # Methods of the queryset = https://docs.djangoproject.com/en/5.0/ref/models/querysets/

        # Subquery to get related_field values from RelatedModel
        # take the list of UserProfile id with the same approver as the logged in user -> it is a list
        subquery = UserProfile.objects.filter(approver=id_approverHere).values('id')

        # Filter MyModel using the subquery
        # return the list of absence request with this filter
        return AbsenceRequest.objects.filter(requester__in=Subquery(subquery))



    # I need to create a different class?
    # TODO: how to accept partial update???
    # patch status only of my team
    def patch(self, request, *args, **kwargs):
        """
            The manager (approver) can modify only the status of the absences, not the other fields
            This operation uses the primary key of AbsenceRequest as pk in the URL.
            The absenceRequests modifiable are the ones selected by the method get_query and are already
            only the ones that the approver can approve.

            Validations done:
            - the approver cannot change the status of the Sick Leave (it is approved automatically)
            - only the status can be changed, the other fields are ignored without a warning

        """
        # get the object
        instance = self.get_object()  # a single object: focusing on pk implicit
        # get the new quality via the serializer
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # validate: TODO: need to change here???
        serializer.is_valid(raise_exception=True)
        # update the data into the DB
        serializer.save()
        # return
        return Response(serializer.data, status=status.HTTP_200_OK)

