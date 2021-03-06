# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 05:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incoming_date', models.DateTimeField(verbose_name='date incoming')),
                ('incoming_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=128)),
                ('material_code', models.CharField(max_length=20)),
                ('control_code', models.CharField(max_length=20)),
                ('Pallet_unit', models.IntegerField(default=1)),
                ('Box_unit', models.IntegerField(default=1)),
                ('unit', models.CharField(default='BOX', max_length=10)),
                ('memo', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Outgoing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outgoing_date', models.DateTimeField(verbose_name='date outgoing')),
                ('outgoing_count', models.IntegerField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Packing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Packing_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pallet', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pallet',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Zone'),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='outgoing_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Unit'),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='packing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Packing'),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='pallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Pallet'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='incoming_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Unit'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Material'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='pallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Pallet'),
        ),
    ]
