# Generated by Django 5.0.1 on 2024-02-01 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_users_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="users",
            old_name="date_of_birth",
            new_name="birthdate",
        ),
    ]
