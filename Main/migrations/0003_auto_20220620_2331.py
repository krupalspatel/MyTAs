# Generated by Django 3.0.14 on 2022-06-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20220617_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ta',
            name='mail',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
