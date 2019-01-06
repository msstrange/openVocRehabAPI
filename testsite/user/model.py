from django.db import models
from django.contrib.auth.models import User
from testsite.application.model import Application
from testsite.models.eligibility import Eligibility
from testsite.models.order_of_selection import OrderOfSelection
from testsite.models.disability import Disability
from testsite.models.trial_work_experience import TrialWorkExperience
from testsite.models.individualized_plan_for_employment import IndividualizedPlanForEmployment
from testsite.models.pre_employment_transition_services import PreemploymentTransitionServices
from testsite.models.VR_SE_service import VrSeService
from testsite.models.career_services import CareerServices
from testsite.models.other_service import OtherService
from testsite.models.measurable_skill_gains import MeasurableSkillGains
from testsite.models.employment import Employment
from testsite.models.exit import Exit
from testsite.models.post_exit import PostExit


# Connects Django user to their vr related information.


class VrUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    application = models.OneToOneField(Application, on_delete='PROTECT', null=True)
    eligibility = models.OneToOneField(Eligibility, on_delete='PROTECT', null=True)
    order_of_selection = models.OneToOneField(OrderOfSelection, on_delete='PROTECT', null=True)
    disability = models.OneToOneField(Disability, on_delete='PROTECT', null=True)
    trial_work_experience = models.OneToOneField(TrialWorkExperience, on_delete='PROTECT', null=True)
    ipe = models.OneToOneField(IndividualizedPlanForEmployment, on_delete='PROTECT', null=True)
    pre_employment_transition_services = models.OneToOneField(
        PreemploymentTransitionServices, on_delete='PROTECT', null=True)
    VR_SE_service = models.OneToOneField(VrSeService, on_delete='PROTECT', null=True)
    career_services = models.OneToOneField(CareerServices, on_delete='PROTECT', null=True)
    other_service = models.OneToOneField(OtherService, on_delete='PROTECT', null=True)
    measurable_skill_gains = models.OneToOneField(MeasurableSkillGains, on_delete='PROTECT', null=True)
    employment = models.OneToOneField(Employment, on_delete='PROTECT', null=True)
    exit = models.OneToOneField(Exit, on_delete='PROTECT', null=True)
    post_exit = models.OneToOneField(PostExit, on_delete='PROTECT', null=True)
