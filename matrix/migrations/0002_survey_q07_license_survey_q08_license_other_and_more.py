# Generated by Django 4.1.3 on 2022-11-23 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matrix", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="q07_license",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q08_license_other",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q08_license_other_Institutional",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q08_license_other_none",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q09_open_data",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q11_specialized_software_open_source",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q12_specialized_software",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q12_specialized_software_specify",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q13_existing_libraries",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q14_nano_publications",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q15_data_formats_csv",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q15_data_formats_database",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q15_data_formats_hd5f",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q15_data_formats_json",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q15_data_formats_other",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q15_data_formats_other_value",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="survey",
            name="q15_data_formats_spreadsheet",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AlterField(
            model_name="survey",
            name="q01_products",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AlterField(
            model_name="survey",
            name="q02_project_name",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AlterField(
            model_name="survey",
            name="time_stamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]