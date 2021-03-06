# Generated by Django 3.2.8 on 2022-01-29 13:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisatie',
            fields=[
                ('nummer', models.IntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)])),
                ('naam', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['-naam'],
            },
        ),
    ]
