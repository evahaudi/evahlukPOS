# Generated by Django 5.0.1 on 2024-02-04 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_userprofile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="birthdate",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="department",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="email",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="experienceyears",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="fullname",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="location",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="phone",
        ),
    ]
