<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 2.1.15 on 2020-10-27 23:11

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 2.1.15 on 2020-10-24 04:34

import django.contrib.postgres.fields
from django.db import migrations, models
>>>>>>> records changes to db
=======
# Generated by Django 2.1.15 on 2020-11-12 01:30

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
>>>>>>> migration changes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Floors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
<<<<<<< HEAD
                ('number', models.IntegerField()),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Buildings')),
=======
                ('building_id', models.IntegerField()),
                ('number', models.IntegerField()),
>>>>>>> records changes to db
=======
                ('number', models.IntegerField()),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Buildings')),
>>>>>>> migration changes
            ],
        ),
        migrations.CreateModel(
            name='Heatmaps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
<<<<<<< HEAD
=======
                ('user_id', models.IntegerField()),
>>>>>>> records changes to db
=======
>>>>>>> migration changes
                ('probabilities', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=10, max_digits=11), size=None), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
<<<<<<< HEAD
                ('room_number', models.IntegerField()),
                ('max_occupancy', models.IntegerField()),
                ('blueprint', models.URLField()),
                ('flood_od', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Floors')),
=======
                ('floor_id', models.IntegerField()),
                ('room_number', models.IntegerField()),
                ('max_occupancy', models.IntegerField()),
                ('blueprint', models.URLField()),
>>>>>>> records changes to db
=======
                ('room_number', models.IntegerField()),
                ('max_occupancy', models.IntegerField()),
                ('blueprint', models.URLField()),
                ('floor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Floors')),
>>>>>>> migration changes
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> migration changes
        migrations.AddField(
            model_name='heatmaps',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Users'),
        ),
<<<<<<< HEAD
=======
>>>>>>> records changes to db
=======
>>>>>>> migration changes
    ]
