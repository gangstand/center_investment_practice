# Generated by Django 4.1.7 on 2023-04-08 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
    ]
