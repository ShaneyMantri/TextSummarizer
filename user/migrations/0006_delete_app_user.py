# Generated by Django 3.0.4 on 2020-04-10 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200410_1542'),
    ]

    operations = [
        migrations.DeleteModel(
            name='app_user',
        ),
    ]
