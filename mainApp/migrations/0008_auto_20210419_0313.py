# Generated by Django 3.1.7 on 2021-04-19 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_auto_20210417_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='images/'),
        ),
    ]
