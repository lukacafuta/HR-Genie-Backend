from django.contrib.auth import get_user_model
from django.db import models

# use custom user: to link
#from customUser.models import CustomUser
CustomUser = get_user_model()

from department.models import Department
from companiesProfile.models import CompaniesProfile

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)

    customUser = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, related_name='userProfile')

    birthdayDate = models.DateField(blank=True, null=True)
    firstDayAtWork = models.DateField(blank=True, null=True)

    # company
    company = models.ForeignKey(to=CompaniesProfile, on_delete=models.CASCADE, default=1)

    # department
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE, default=1)

    GENDER_CASES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=11, choices=GENDER_CASES, default='pending')

    # who is the approver of this user: 1-to-many to the same model
    # maybe remove blank and null?
    #approver = models.OneToOneField('self', related_name='teamMember', on_delete=models.CASCADE, default=1) #null=True, blank=True)
    approver = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinate')


    isCompanyAdmin = models.BooleanField(default=False)


