from django.db import models


class OrderOfSelection(models.Model):

    date_of_placement = models.DateField()
    date_of_exit = models.DateField()
