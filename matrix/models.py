from django.db import models


class Survey(models.Model):
    q01_products = models.CharField(max_length=256)
    q02_project_name = models.CharField(max_length=256)
    time_stamp = models.DateField(auto_now_add=True)
