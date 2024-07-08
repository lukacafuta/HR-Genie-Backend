# Generated by Django 5.0.6 on 2024-07-06 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("userProfile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeDependentVar",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("startDate", models.DateField()),
                ("endDate", models.DateField()),
                (
                    "variable",
                    models.CharField(
                        choices=[
                            ("nr_tot_vacation_days", "Total Vacation Days"),
                            ("pensum_perc", "Pensum %"),
                            ("maternity_leave", "Maternity Leave"),
                            ("nr_working_hours_per_week", "Working Hours per Week"),
                        ],
                        default="nr_tot_vacation_days",
                        max_length=25,
                    ),
                ),
                ("value", models.FloatField()),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timeDepVars",
                        to="userProfile.userprofile",
                    ),
                ),
            ],
        ),
    ]
