# Generated by Django 3.1.3 on 2021-01-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210116_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='ToDo1',
        ),
    ]
