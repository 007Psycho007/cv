# Generated by Django 4.0.2 on 2022-02-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperiences',
            name='location',
            field=models.CharField(default="None", max_length=255),
            preserve_default=False,
        ),
    ]
