import graphene
from django.contrib.auth.models import User
from .model import VrUser


class CreateUser(graphene.Mutation):

    username = graphene.String()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, username, email, password, first_name, last_name):

        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        vr_user = VrUser(user=user)
        vr_user.save()

        return CreateUser(
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )
