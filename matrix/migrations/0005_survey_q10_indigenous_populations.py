# Generated by Django 4.1.3 on 2022-11-23 04:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("matrix", "0004_alter_survey_q01_products_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="q10_indigenous_populations",
            field=models.CharField(blank=True, default="", max_length=256),
        ),
    ]
