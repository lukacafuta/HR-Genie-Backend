# Generated by Django 5.0.6 on 2024-07-04 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_alter_userprofile_approver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinate', to='userProfile.userprofile'),
        ),
    ]