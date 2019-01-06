import graphene
from graphene_django.types import DjangoObjectType
from open_vr_api.models.individual_characterists import IndividualCharacteristics


class UserType(DjangoObjectType):
    class Meta:
        model = IndividualCharacteristics
