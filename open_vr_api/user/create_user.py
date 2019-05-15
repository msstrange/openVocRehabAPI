import graphene
from django.contrib.auth.models import User
from .model import VrUser


class CreateUser(graphene.Mutation):

    username = graphene.String(required=True)
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    success = graphene.Boolean(required=True)
    user_already_exists = graphene.Boolean(required=True)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    def mutate(self, info, username, email, password, first_name, last_name):

        if User.objects.filter(username=username).exists():

            return CreateUser(
                username=username,
                success=False,
                user_already_exists=True
            )

        user = User(username=username,
                     email=email,
                     password=password,
                     first_name=first_name,
                     last_name=last_name)

        user.save()
        vr_user = VrUser(user=user)
        vr_user.save()

        return CreateUser(
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            success=True,
            user_already_exists=False
        )
