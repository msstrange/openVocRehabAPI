from django.db import models
from testsite.models.individualized_plan_for_employment import IndividualizedPlanForEmployment


class VocationalCredentialLicense(models.Model):
    not_leading_to_postsecondary_credential = models.BooleanField()
    leading_to_postsecondary_credential = models.BooleanField()
    date_vocational_license = models.DateField(null=True)
    date_vocational_certificate = models.DateField(null=True)
