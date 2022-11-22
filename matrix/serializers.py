from rest_framework import serializers
from .models import Survey


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ["q01_products", "q02_project_name", "time_stamp"]
