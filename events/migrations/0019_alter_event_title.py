# Generated by Django 4.1.1 on 2022-12-04 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_alter_event_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=128, unique=True, validators=[django.core.validators.MaxLengthValidator(128)]),
        ),
    ]
