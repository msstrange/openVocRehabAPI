import graphene
from open_vr_api.user.model import VrUser
from .model import Support
from .type import SupportType


class CreateSupport(graphene.Mutation):

    class Arguments:
        ssdi = graphene.Boolean(required=True)
        ssi = graphene.Boolean(required=True)
        tanf = graphene.Boolean(required=True)
        general_assistance = graphene.Boolean(required=True)
        veterans_disability = graphene.Boolean(required=True)
        workers_compensation = graphene.Boolean(required=True)
        unemployment_insurance = graphene.Boolean(required=True)
        primary_source_support = graphene.Int(required=True)

    support = graphene.Field(SupportType)

    def mutate(self, info, ssdi, ssi, tanf,
               general_assistance, veterans_disability, workers_compensation, unemployment_insurance, primary_source_support):

        if not info.context.user.is_anonymous:

            this_user = VrUser.objects.get(user=info.context.user)

            support = Support(

                ssdi=ssdi,
                ssi=ssi,
                tanf=tanf,
                general_assistance=general_assistance,
                veterans_disability=veterans_disability,
                workers_compensation=workers_compensation,
                unemployment_insurance=unemployment_insurance,
                primary_source_support=primary_source_support

            )

            support.save()

            this_user.application.support = support

            this_user.application.support.save()

            return CreateSupport(

                support=support

            )

        else:

            raise Exception("User not authenticated.")
