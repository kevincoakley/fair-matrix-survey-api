from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets

from .serializers import SurveySerializer
from .models import Survey


def index(request):
    return render(request, "matrix/index.html")


def detail(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, "matrix/detail.html", {"survey": survey})


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all().order_by("time_stamp")
    serializer_class = SurveySerializer
