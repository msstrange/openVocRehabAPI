import graphene
import graphql_jwt
from .user.create_user import CreateUser
from .application.create_application import CreateApplication
from .individual_characteristics.create_individual_characteristics import CreateIndividualCharacteristics
from .location_information.create_location_information import CreateLocationInformation
from .medical_insurance_coverage.create_medical_insurance_coverage import CreateMedicalInsuranceCoverage
from .support.create_support import CreateSupport


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
    create_individual_characteristics = CreateIndividualCharacteristics.Field()
    create_location_information = CreateLocationInformation.Field()
    create_medical_insurance_coverage = CreateMedicalInsuranceCoverage.Field()
    create_support = CreateSupport.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
