# Generated by Django 3.0.4 on 2020-04-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200410_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='Profile_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
