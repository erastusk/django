# Generated by Django 4.0.2 on 2022-03-06 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_cities',
            old_name='user_id',
            new_name='user',
        ),
    ]
