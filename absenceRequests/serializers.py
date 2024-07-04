from rest_framework import serializers
from .models import AbsenceRequest

# import UserProfile to get all the info of the user and manager
from userProfile.serializers import UserProfileSerializerAll,UserProfileSerializerByRequester


class AbsenceSerializerAll(serializers.ModelSerializer):

    # export also from UserProfile:
    # customUser id, company name, dept name, requester first_name and last_name, approver name and last name
    #userData = UserProfileSerializerAll(read_only=True) # many=True, read_only=True)
    requesterData = UserProfileSerializerByRequester(read_only=True)  # many=True, read_only=True)

    # maybe there is more than 1 join and does not know which to use
    # requester_id


    class Meta:
        model = AbsenceRequest
        fields = ['requesterData', 'id', 'requester', 'startDt',
                  'endDt', 'reason', 'status'
                  ]
        #fields = '__all__'
        #fields.append('userData')  # does not work
        # why is userData not printer???

        # test for debugging
        #depth = 1

