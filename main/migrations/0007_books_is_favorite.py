# Generated by Django 3.1.3 on 2021-01-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210119_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
