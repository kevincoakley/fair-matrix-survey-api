# Generated by Django 4.1.3 on 2022-12-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matrix", "0006_survey_q05_products_posted_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="q64_email_address",
            field=models.CharField(blank=True, default="", max_length=256),
        ),
    ]
