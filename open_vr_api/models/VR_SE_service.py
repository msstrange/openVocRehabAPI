from django.db import models
from open_vr_api.models.service import Service


class VrSeService(models.Model):

    initial_vr_start_date = models.DateField()
    most_recent_career_service = models.DateField()
    graduate_college_university = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='graduate_college_university')

    four_year_college = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='four_year_college')

    junior_community_college = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='junior_community_college')

    occupational_vocational_training = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='occupational_vocational_training')

    on_the_job_training = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='on_the_job_training')

    registered_apprenticeship_training = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='registered_apprenticeship_training')

    basic_academic_training = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='basic_academic_training')

    job_readiness_training = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='job_readiness_training')

    disability_related_skills = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='disability_related_skills')

    miscellaneous_training = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='miscellaneous_training')

    randolph_sheppard_entrependeurial = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='randolph_sheppard_entrependeurial')

    customized_training = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='customized_training')

