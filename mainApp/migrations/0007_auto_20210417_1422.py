# Generated by Django 3.1.7 on 2021-04-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_userprofile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]
