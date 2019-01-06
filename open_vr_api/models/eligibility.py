from django.db import models


class Eligibility(models.Model):

    date = models.DateField()
    has_extension = models.BooleanField()
