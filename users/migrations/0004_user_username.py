# Generated by Django 4.0.5 on 2022-06-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
    ]
