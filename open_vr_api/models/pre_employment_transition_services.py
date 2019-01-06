from django.db import models
from open_vr_api.models.service import Service


class PreemploymentTransitionServices(models.Model):

    start_date = models.DateField()
    job_exploration_counseling = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='job_exploration_counseling')

    work_based_learning = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='work_based_learning')

    counseling_on_enrollment = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='counseling_on_enrollment')

    workplace_readiness_training = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='workplace_readiness_training')

    instruction_in_self_advocacy = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='instruction_in_self_advocacy')
