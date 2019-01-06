import graphene
from graphene_django.types import DjangoObjectType
from testsite.models.individual_characterists import IndividualCharacteristics


class UserType(DjangoObjectType):
    class Meta:
        model = IndividualCharacteristics
