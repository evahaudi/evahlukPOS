# Generated by Django 5.0.1 on 2024-01-31 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_users_name_users_fullname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Chef", "Chef"),
                    ("Manager", "Manager"),
                    ("Waiter", "Waiter"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
