# Generated by Django 4.0.5 on 2022-06-27 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_created_at_remove_user_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
