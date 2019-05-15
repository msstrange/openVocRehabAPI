from graphene_django.types import DjangoObjectType
from .model import IndividualCharacteristics


class IndividualCharacteristicsType(DjangoObjectType):
    class Meta:
        model = IndividualCharacteristics
