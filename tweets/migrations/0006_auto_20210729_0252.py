# Generated by Django 2.2.13 on 2021-07-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20200602_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='user.png', null=True, upload_to=''),
        ),
    ]