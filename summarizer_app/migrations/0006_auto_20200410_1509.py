# Generated by Django 3.0.4 on 2020-04-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer_app', '0005_auto_20200407_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_received',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
