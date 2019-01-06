from django.db import models


class MedicalInsuranceCoverage(models.Model):

    medicaid_at_application = models.BooleanField()
    medicare_at_application = models.BooleanField()
    affordable_care_exchange = models.BooleanField()
    public_insurance_from_other_source = models.BooleanField()
    private_insurance_through_employer = models.BooleanField()
    not_yet_eligible_for_private_insurance = models.BooleanField()
    other_private_insurance = models.BooleanField()
