# Generated by Django 2.2.5 on 2019-09-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeCard', '0005_auto_20190927_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='time_in',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='timecard',
            name='time_out',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
