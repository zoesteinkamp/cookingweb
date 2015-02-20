# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('rating', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Pinch', 'Pinch'), ('Pounds', 'Pounds'), ('Whole', 'Whole'), ('Teaspoon', 'Teaspoon'), ('Tablespoon', 'Tablespoon'), ('Cups', 'Cups')], max_length=20)),
                ('amount', models.CharField(choices=[('Pinch', (('1', '1'),)), ('Teaspoon', (('1/8', '1/8'), ('1/4', '1/4'), ('1/2', '1/2'), ('1', 'one'), ('1 1/2', '1 1/2'), ('2', 'two'))), ('Tablespoon', (('1/2', 'half'), ('1', 'one'), ('1 1/2', '1 1/2'), ('2', 'two'), ('2 1/2', '2 1/2'), ('3', 'three'))), ('Cup', (('1/4', '1/4'), ('1/3', '1/3'), ('1/2', '1/2'), ('2/3', '2/3'), ('3/4', '3/4'), ('1', 'one'), ('1 1/4', '1 1/4'), ('1 1/3', '1 1/3'), ('1 1/2', '1 1/2'), ('1 2/3', '1 2/3'), ('1 3/4', '1 3/4'), ('2', 'two'), ('2 1/4', '2 1/4'), ('2 1/3', '2 1/3'), ('2 1/2', '2 1/2'), ('2 2/3', '2 2/3'), ('2 3/4', '2 3/4'), ('3', 'three'), ('3 1/4', '3 1/4'), ('3 1/3', '3 1/3'), ('3 1/2', '3 1/2'), ('3 2/3', '3 2/3'), ('3 3/4', '3 3/4'), ('4', 'four'), ('4 1/4', '4 1/4'), ('4 1/3', '4 1/3'), ('4 1/2', '4 1/2'), ('4 2/3', '4 2/3'), ('4 3/4', '4 3/4'), ('5', 'five'), ('5 1/4', '5 1/4'), ('5 1/3', '5 1/3'), ('5 1/2', '5 1/2'), ('5 2/3', '5 2/3'), ('5 3/4', '5 3/4'))), ('Pounds', (('1/4', '1/4'), ('1/3', '1/3'), ('1/2', '1/2'), ('2/3', '2/3'), ('3/4', '3/4'), ('1', 'one'), ('1 1/4', '1 1/4'), ('1 1/3', '1 1/3'), ('1 1/2', '1 1/2'), ('1 2/3', '1 2/3'), ('1 3/4', '1 3/4'), ('2', 'two'), ('2 1/4', '2 1/4'), ('2 1/3', '2 1/3'), ('2 1/2', '2 1/2'), ('2 2/3', '2 2/3'), ('2 3/4', '2 3/4'), ('3', 'three'), ('3 1/4', '3 1/4'), ('3 1/3', '3 1/3'), ('3 1/2', '3 1/2'), ('3 2/3', '3 2/3'), ('3 3/4', '3 3/4'), ('4', 'four'), ('4 1/4', '4 1/4'), ('4 1/3', '4 1/3'), ('4 1/2', '4 1/2'), ('4 2/3', '4 2/3'), ('4 3/4', '4 3/4'), ('5', 'five'), ('5 1/4', '5 1/4'), ('5 1/3', '5 1/3'), ('5 1/2', '5 1/2'), ('5 2/3', '5 2/3'), ('5 3/4', '5 3/4'))), ('Whole Items', (('1/2', '1/2'), ('1', 'one'), ('1 1/2', '1 1/2'), ('2', 'two'), ('2 1/2', '2 1/2'), ('3', 'three'), ('3 1/2', '3 1/2'), ('4', 'four'), ('4 1/2', '4 1/2'), ('5', 'five'), ('5 1/2', '5 1/2'), ('6', '6')))], max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('image_main', models.ImageField(upload_to='%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=40)),
                ('short_des', models.TextField(max_length=200)),
                ('long_des', models.TextField()),
                ('servings', models.IntegerField()),
                ('prep_time', models.IntegerField()),
                ('cook_time', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='date created')),
                ('vegan', models.NullBooleanField(default=False)),
                ('vegeterian', models.NullBooleanField(default=False)),
                ('glutten_free', models.NullBooleanField(default=False)),
                ('dairy_free', models.NullBooleanField(default=False)),
                ('slug', models.SlugField()),
                ('ingredients', models.ManyToManyField(to='Recipes.Ingredients')),
                ('photo', models.ForeignKey(to='Recipes.MainPhoto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tag', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='Recipes.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(to='Recipes.Recipe'),
            preserve_default=True,
        ),
    ]
