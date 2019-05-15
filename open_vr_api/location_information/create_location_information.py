import graphene
from open_vr_api.user.model import VrUser
from .model import LocationInformation
from .type import LocationInformationType


class CreateLocationInformation(graphene.Mutation):

    class Arguments:
        postal_code = graphene.String(required=True)
        fips_code = graphene.String(required=True)
        zip_code = graphene.String(required=True)

    location_information = graphene.Field(LocationInformationType)

    def mutate(self, info, postal_code, fips_code, zip_code):

        if not info.context.user.is_anonymous:

            this_user = VrUser.objects.get(user=info.context.user)

            location_information = LocationInformation(

                postal_code=postal_code, fips_code=fips_code, zip_code=zip_code

            )

            location_information.save()

            this_user.application.location_information = location_information

            this_user.application.location_information.save()

            return CreateLocationInformation(

                location_information=location_information

            )

        else:

            raise Exception("User not authenticated.")