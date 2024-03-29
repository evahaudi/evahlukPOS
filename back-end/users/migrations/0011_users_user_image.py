# Generated by Django 5.0.1 on 2024-02-04 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_remove_userprofile_birthdate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="user_image",
            field=models.ImageField(
                default="default_user_image.jpg", upload_to="user_images/"
            ),
        ),
    ]
