from rest_framework import serializers
from .models import AbsenceRequest

# import UserProfile to get all the info of the user and manager
from userProfile.serializers import UserProfileSerializerAll, UserProfileSerializerByRequester


class AbsenceSerializerAll(serializers.ModelSerializer):

    # export also from UserProfile:
    # customUser id, company name, dept name, requester first_name and last_name, approver name and last name
    #userData = UserProfileSerializerAll(read_only=True) # many=True, read_only=True)
    #requester = UserProfileSerializerByRequester(read_only=True)  # many=True, read_only=True)

    # maybe there is more than 1 join and does not know which to use
    # requester_id


    class Meta:
        model = AbsenceRequest
        fields = ['id', 'requester', 'startDt',
                  'endDt', 'reason', 'status', 'dtCreated', 'dtUpdated'
                  ]
        read_only_fields = ['requester', 'status']  # cannot be modified
        #fields = '__all__'
        #fields.append('userData')  # does not work
        # why is userData not printer???

        # test for debugging
        #depth = 1

    def validate(self, data):
        if data['startDt'] >= data['endDt']:
            raise serializers.ValidationError("startDt must occur before endDt")
        return data




# ...............................................................................
"""
    This serializer is to be used with the manager:
    PATCH only the status and not the other fields
    PATCH only if not sick_leave
"""
class AbsenceSerializerManager(serializers.ModelSerializer):

    # export also from UserProfile:
    # customUser id, company name, dept name, requester first_name and last_name, approver name and last name
    # userData = UserProfileSerializerAll(read_only=True) # many=True, read_only=True)
    #requesterData = UserProfileSerializerByRequester(read_only=True)  # many=True, read_only=True)

    class Meta:
        model = AbsenceRequest
        fields = ['id', 'status', 'reason'] #, 'requester', 'reason']
        read_only_fields = ['reason']
        # read_only_fields = ['requester', 'reason', 'status']  # cannot be modified
        #fields = '__all__'
        #fields.append('userData')  # does not work
        # why is userData not printer???

        # test for debugging
        #depth = 1

    # apparently the data selected are already the ones in the query_selected in the view
    def validate(self, data):
        # only change the ones of my team -> already like this in get_queryset
        # only accepted 'approved' or 'rejected' not pending -> but he can change his mind -> do not do it


        # Access the instance being updated (with all fields, also the ones not passed)
        instance = self.instance

        # If reason = 'sick_leave' -> not possible to change
        if (instance.reason == 'sick_leave'):
            raise serializers.ValidationError('You cannot change the status of Sick Leave')
        else:
            return data


    #def validate(self, data):
    #    if data['startDt'] >= data['endDt']:
    #        raise serializers.ValidationError("startDt must occur before endDt")
    #    return data

