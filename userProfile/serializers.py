from rest_framework import serializers
from .models import UserProfile
from customUser.serializers import CustomUserSerializerPrivate


#from ..customUser.serializers import CustomUserSerializerPrivate


# other serializers for other fields
#from companiesProfile.serializers import CompaniesProfileSerializer
#from customUser.serializers import CustomUserSerializerPrivate


# get custom model
# customUser = get_user_model()

# ..........................................................
class UserProfileSerializerAll(serializers.ModelSerializer):

    # nest here from CustomUser: first_name, last_name
    # nest here from companiesProfile: nameCompany
    # nest here from department: nameDepartment
    # nest from UserProfile: first_name e last_name of the approver

    #  company_data = CompaniesProfileSerializer(read_only=True)
    #  userId = CustomUserSerializerPrivate(read_only=True)
    requester_data = CustomUserSerializerPrivate(read_only=True)
    #  userId = CustomUserSerializerPrivate(read_only=True)

    class Meta:
        model = UserProfile
        #  fields = '__all__'
        #  fields = ['id', 'customUser', 'requester_data', 'approver', 'company', 'company_data' ]
        fields = ['id', 'customUser', 'requester_data', 'approver', 'company']
        #  fields = ['id', 'customUser', 'userId', 'approver', 'company']




#  ..........................................................
# this serializer below is needed to fetch the data of the requester of
# AbsenceRequest and TrainingRequest
class UserProfileSerializerByRequester(serializers.ModelSerializer):

    # nest here from CustomUser: first_name, last_name
    # nest here from companiesProfile: nameCompany
    # nest here from department: nameDepartment
    # nest from UserProfile: first_name e last_name of the approver



    class Meta:
        model = UserProfile
        #fields = '__all__'
        fields = ('approver', 'company', 'department', 'customUser')

