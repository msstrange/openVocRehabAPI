import graphene
import graphql_jwt
from .user.create_user import CreateUser
from .application.create_application import CreateApplication


class Query(graphene.ObjectType):
    pass


class Query(graphene.ObjectType):
    create_user = CreateUser.Field()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_application = CreateApplication.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
