from django.db import models


class TrialWorkExperience(models.Model):

    start_date = models.DateField()
    end_date = models.DateField()
