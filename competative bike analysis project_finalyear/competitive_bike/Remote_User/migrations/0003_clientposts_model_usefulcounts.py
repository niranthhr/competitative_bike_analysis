# Generated by Django 2.0.5 on 2019-04-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Remote_User', '0002_clientposts_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientposts_model',
            name='uname',
            field=models.IntegerField(default=0),
        ),
    ]
