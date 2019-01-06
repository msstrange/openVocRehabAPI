import graphene
from graphene_django.types import DjangoObjectType
from .model import IndividualCharacteristics


class ApplicationType(DjangoObjectType):
    class Meta:
        model = IndividualCharacteristics
