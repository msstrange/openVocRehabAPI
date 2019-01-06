from django.db import models
from testsite.models.ipe_employment import IpeEmployment
from testsite.models.WIOA_program_involvement import WIOAProgramInvolvement


class IndividualizedPlanForEmployment(models.Model):

    created_or_appended = models.DateField
    supported_employment_goal = models.BooleanField
    employment = models.OneToOneField(IpeEmployment, on_delete='PROTECT')
    wioa_program_involvement = models.OneToOneField(WIOAProgramInvolvement, on_delete='PROTECT')
    date_other_diploma = models.DateField(null=True)
