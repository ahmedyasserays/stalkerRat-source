# Generated by Django 3.1.7 on 2021-04-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20210415_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
