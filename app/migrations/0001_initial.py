# Generated by Django 3.1.7 on 2021-03-24 17:48

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Floors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=2)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.buildings')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=4)),
                ('max_occupancy', models.IntegerField()),
                ('max_pandemic_occupancy', models.IntegerField(null=True)),
                ('blueprint', models.URLField(null=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.floors')),
            ],
        ),
        migrations.CreateModel(
            name='Heatmaps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probabilities', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=10, max_digits=11), size=None), size=None)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.rooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.users')),
            ],
        ),
    ]
