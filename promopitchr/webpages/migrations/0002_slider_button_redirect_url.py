# Generated by Django 4.2.3 on 2023-07-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_redirect_url',
            field=models.TextField(default='https://www.google.com'),
        ),
    ]