from django.db import models

from userProfile.models import UserProfile


# Create your models here.
class TimeDependentVar(models.Model):
    id = models.AutoField(primary_key=True)

    startDate = models.DateField()
    endDate = models.DateField()

    POSSIBLE_VAR = [
        ('nr_tot_vacation_days', 'Total Vacation Days'),
        ('pensum_perc', 'Pensum %'),
        ('maternity_leave', 'Maternity Leave'),
        ('nr_working_hours_per_week', 'Working Hours per Week')
    ]
    variable = models.CharField(max_length=25, choices=POSSIBLE_VAR, default='nr_tot_vacation_days')

    value = models.FloatField() # done as float temporarily

    # link to user profile: here it is many
    user = models.ForeignKey(to=UserProfile, related_name='timeDepVars', on_delete=models.CASCADE, default=1)
