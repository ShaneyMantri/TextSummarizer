# Generated by Django 3.0.4 on 2020-04-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_received',
            name='image',
            field=models.ImageField(upload_to='photos_to_summarize'),
        ),
    ]
