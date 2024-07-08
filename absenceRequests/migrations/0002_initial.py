# Generated by Django 5.0.6 on 2024-07-08 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('absenceRequests', '0001_initial'),
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='absencerequest',
            name='requester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='absenceRequest_related', to='userProfile.userprofile'),
        ),
    ]
