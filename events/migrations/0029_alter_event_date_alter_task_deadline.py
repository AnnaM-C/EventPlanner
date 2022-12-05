# Generated by Django 4.1.1 on 2022-12-05 20:27

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_alter_event_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date.today)]),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date.today)]),
        ),
    ]
