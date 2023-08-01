# Generated by Django 4.2.3 on 2023-07-28 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('father_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.TextField(max_length=100)),
                ('admission_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
