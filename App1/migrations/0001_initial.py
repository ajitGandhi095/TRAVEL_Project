# Generated by Django 5.2.1 on 2025-05-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('Fname', models.CharField(max_length=30)),
                ('Lname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('gmail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
