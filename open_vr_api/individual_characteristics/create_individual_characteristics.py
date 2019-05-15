import graphene
from open_vr_api.user.model import VrUser
from .model import IndividualCharacteristics
from .type import IndividualCharacteristicsType


class CreateIndividualCharacteristics(graphene.Mutation):

    class Arguments:
        sex = graphene.Int(required=True)
        alaskan_native = graphene.Int(required=True)
        asian = graphene.Int(required=True)
        black = graphene.Int(required=True)
        native_hawaiian = graphene.Int(required=True)
        white = graphene.Int(required=True)
        hispanic = graphene.Int(required=True)
        veteran = graphene.Boolean(required=True)

    individual_characteristics = graphene.Field(IndividualCharacteristicsType)

    def mutate(self, info, sex, alaskan_native, asian,
               black, native_hawaiian, white, hispanic, veteran, living_arrangement):

        if not info.context.user.is_anonymous:

            this_user = VrUser.objects.get(user=info.context.user)

            individual_characteristics = IndividualCharacteristics(

                sex=sex, alaskan_native=alaskan_native, asian=asian, black=black, native_hawaiian=native_hawaiian,
                white=white, hispanic=hispanic, veteran=veteran, living_arrangement=living_arrangement

            )

            individual_characteristics.save()

            this_user.application.individual_characteristics = individual_characteristics

            this_user.application.save()

            return CreateIndividualCharacteristics(

                individual_characteristics=individual_characteristics

            )

        else:

            raise Exception("User not authenticated.")
