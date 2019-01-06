import graphene
from graphene_django.types import DjangoObjectType
from .model import Application


class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application

