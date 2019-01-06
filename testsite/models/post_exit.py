from django.db import models
from testsite.models.quarterly_report import QuarterlyReport


class PostExit(models.Model):

    postsecondary_diploma_equivalency = 1
    aa_as_diploma = 2
    ba_bs_diploma = 3
    graduate_degree_diploma = 4
    occupational_licensure = 5
    occupational_certificate = 6
    occupational_certification = 7
    other_recognized_diploma = 8

    type_of_recognized_credential_choice = (

        (postsecondary_diploma_equivalency, 'PostsecondaryDiploma or Equivalency'),
        (aa_as_diploma, 'AA or AS Diploma/Degree'),
        (ba_bs_diploma, 'BA or BS Diploma/Degree'),
        (graduate_degree_diploma, 'Graduate/Post Graduate Degree/Diploma'),
        (occupational_licensure, 'Occupational Licensure'),
        (occupational_certificate, 'Occupational Certificate'),
        (occupational_certification, 'Occupational Certification'),
        (other_recognized_diploma, 'Other Recognized Diploma, Degree, or Certificate')

    )

    date_enrolled_education = models.DateField()
    date_attainment_credential = models.DateField()

    first_quarter = models.OneToOneField(
        QuarterlyReport, on_delete=models.PROTECT, related_name='first_quarter')

    employment_related_training_second_quarter = models.BooleanField()
    second_quarter = models.OneToOneField(
        QuarterlyReport, on_delete=models.PROTECT, related_name='second_quarter')

    third_quarter = models.OneToOneField(
        QuarterlyReport, on_delete=models.PROTECT, related_name='third_quarter')

    fourth_quarter = models.OneToOneField(
        QuarterlyReport, on_delete=models.PROTECT, related_name='fourth_quarter')
    retention_after_fourth_quarter = models.BooleanField()
