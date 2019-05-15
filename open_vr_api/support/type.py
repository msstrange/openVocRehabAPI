from graphene_django.types import DjangoObjectType
from .model import Support


class SupportType(DjangoObjectType):
    class Meta:
        model = Support
