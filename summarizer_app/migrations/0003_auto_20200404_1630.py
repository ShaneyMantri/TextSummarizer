# Generated by Django 3.0.4 on 2020-04-04 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer_app', '0002_auto_20200404_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_received',
            name='dateTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_received',
            name='username',
            field=models.CharField(default='Defualt', max_length=100),
            preserve_default=False,
        ),
    ]