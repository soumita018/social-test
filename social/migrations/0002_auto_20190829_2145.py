# Generated by Django 2.2.4 on 2019-08-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
