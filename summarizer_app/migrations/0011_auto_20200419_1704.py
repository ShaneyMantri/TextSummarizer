# Generated by Django 3.0.4 on 2020-04-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer_app', '0010_auto_20200419_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_received',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]