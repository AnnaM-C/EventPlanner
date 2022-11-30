# Generated by Django 4.1.1 on 2022-11-29 11:22

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_event_date_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime.today, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.datetime.today)]),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]