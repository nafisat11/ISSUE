# Generated by Django 2.1.15 on 2020-11-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201027_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='max_pandemic_occupancy',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
