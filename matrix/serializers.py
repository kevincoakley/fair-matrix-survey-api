from rest_framework import serializers
from .models import Survey


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = [
            "q01_products",
            "q02_project_name",
            "q05_products_posted",
            "q05_products_posted_other",
            "q06_simulations",
            "q07_license",
            "q08_license_other",
            "q08_license_other_institutional",
            "q08_license_other_none",
            "q09_open_data",
            "q10_indigenous_populations",
            "q11_specialized_software_open_source",
            "q12_specialized_software",
            "q12_specialized_software_specify",
            "q13_existing_libraries",
            "q14_nano_publications",
            "q15_data_formats_csv",
            "q15_data_formats_database",
            "q15_data_formats_hd5f",
            "q15_data_formats_json",
            "q15_data_formats_other",
            "q15_data_formats_other_value",
            "q15_data_formats_spreadsheet",
            "q64_email_address",
            "time_stamp",
        ]
