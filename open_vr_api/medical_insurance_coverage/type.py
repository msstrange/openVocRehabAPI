from graphene_django.types import DjangoObjectType
from .model import MedicalInsuranceCoverage


class MedicalInsuranceCoverageType(DjangoObjectType):
    class Meta:
        model = MedicalInsuranceCoverage
