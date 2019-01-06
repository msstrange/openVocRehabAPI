from django.db import models
from open_vr_api.models.service import Service


class CareerServices(models.Model):

    assessment = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='assessment')

    diagnosis_treatment_impairments = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='diagnosis_treatment_impairments')

    vr_counseling_guidance = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='vr_counseling_guidance')

    job_search_assistance = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='job_search_assistance')

    job_placement_assistance = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='job_placement_assistance')

    short_term_job_support = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='short_term_job_support')

    supported_employment_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='supported_employment_services')

    information_referral_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='information_referral_services')

    benefits_counseling = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT,related_name='benefits_counseling')

    customized_employment_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='customized_employment_services')

    extended_services = models.OneToOneField(
        Service, null=True, on_delete=models.PROTECT, related_name='extended_services')
