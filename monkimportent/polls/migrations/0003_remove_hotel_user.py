# Generated by Django 3.1.4 on 2021-06-06 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_hotel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='user',
        ),
    ]