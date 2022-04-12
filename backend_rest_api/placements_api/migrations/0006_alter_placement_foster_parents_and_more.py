# Generated by Django 4.0.3 on 2022-04-12 18:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements_api', '0005_alter_placement_foster_parents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='foster_parents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='placement',
            name='foster_siblings',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
    ]