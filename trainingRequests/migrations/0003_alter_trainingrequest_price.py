# Generated by Django 5.0.7 on 2024-07-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trainingRequests", "0002_alter_trainingrequest_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainingrequest",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
