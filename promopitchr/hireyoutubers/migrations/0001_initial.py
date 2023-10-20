# Generated by Django 4.2.3 on 2023-07-17 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hireyoutuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('youtuber_id', models.IntegerField(blank=True)),
                ('youtuber_name', models.CharField(max_length=255)),
                ('user_id', models.IntegerField(blank=True)),
                ('city', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('state', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
                ('email', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
