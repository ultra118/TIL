# Generated by Django 2.2.1 on 2019-06-19 07:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_boards', to=settings.AUTH_USER_MODEL),
        ),
    ]
