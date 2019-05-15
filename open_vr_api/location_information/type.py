from graphene_django.types import DjangoObjectType
from .model import LocationInformation


class LocationInformationType(DjangoObjectType):
    class Meta:
        model = LocationInformation
