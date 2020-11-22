# Generated by Django 2.1.15 on 2020-11-19 20:45

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Floors',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('building', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='app.Buildings')),
            ],
        ),
        migrations.CreateModel(
            name='Heatmaps',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('probabilities', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(
                    base_field=models.DecimalField(decimal_places=10, max_digits=11), size=None), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('max_occupancy', models.IntegerField()),
                ('max_pandemic_occupancy', models.IntegerField()),
                ('blueprint', models.URLField()),
                ('floor', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='app.Floors')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='heatmaps',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='app.Users'),
        ),
    ]
