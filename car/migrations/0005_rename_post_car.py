# Generated by Django 4.2.4 on 2023-08-31 18:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0004_remove_userprofile_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Car',
        ),
    ]