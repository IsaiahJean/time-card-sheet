# Generated by Django 2.2.5 on 2019-09-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeCard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='hours_worked',
            field=models.TimeField(),
        ),
    ]
