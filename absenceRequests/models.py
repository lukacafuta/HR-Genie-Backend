from django.db import models

from userProfile.models import UserProfile


# Create your models here.
class AbsenceRequest(models.Model):
    id = models.AutoField(primary_key=True)

    # TODO:
    requester = models.ForeignKey(to=UserProfile, related_name='absenceRequest', on_delete=models.CASCADE, default=1)

    startDt = models.DateTimeField()
    endDt = models.DateTimeField()

    reason = models.CharField(max_length=300)

    STATUS_APPROVAL = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=11, choices=STATUS_APPROVAL, default='pending')

    # TODO: relate to the MediaLink table
    #attachmentsId =

    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)
