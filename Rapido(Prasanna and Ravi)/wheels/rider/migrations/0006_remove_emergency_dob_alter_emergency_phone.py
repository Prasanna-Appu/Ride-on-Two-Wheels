# Generated by Django 4.1 on 2022-08-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0005_careers_delete_registerasrider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergency',
            name='DOB',
        ),
        migrations.AlterField(
            model_name='emergency',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
