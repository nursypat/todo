# Generated by Django 3.1.3 on 2021-01-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210118_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]
