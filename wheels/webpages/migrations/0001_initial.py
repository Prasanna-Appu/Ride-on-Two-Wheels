# Generated by Django 4.1 on 2022-08-09 11:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutJumbo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=60)),
                ('subhead', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutJumbo2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=60)),
                ('subhead', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutJumbo3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=60)),
                ('subhead', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.IntegerField()),
                ('address', ckeditor.fields.RichTextField()),
                ('message', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/home/cards/%Y/')),
                ('city', models.CharField(max_length=60)),
                ('desc', ckeditor.fields.RichTextField()),
                ('rto_no', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='HomeCurosol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/home/cursol/%Y/')),
                ('head', models.CharField(max_length=60)),
                ('subhead', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeJumbotron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=60)),
                ('subhead', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/services/cards/%Y/')),
                ('city', models.CharField(max_length=60)),
                ('subhead', ckeditor.fields.RichTextField()),
                ('button_text', models.CharField(max_length=20)),
            ],
        ),
    ]
