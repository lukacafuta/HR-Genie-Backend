# Generated by Django 5.0.6 on 2024-07-08 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompaniesProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=100)),
            ],
        ),
    ]
