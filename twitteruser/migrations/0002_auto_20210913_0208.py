# Generated by Django 3.2.7 on 2021-09-13 02:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweeteruser',
            name='follower',
        ),
        migrations.AddField(
            model_name='tweeteruser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='_twitteruser_tweeteruser_followers_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
