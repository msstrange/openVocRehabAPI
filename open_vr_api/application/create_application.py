import graphene
from open_vr_api.user.model import VrUser
from .model import Application
from .type import ApplicationType
import datetime


class CreateApplication(graphene.Mutation):

    class Arguments:
        date_of_birth = graphene.Date(required=True)
        source_of_referral = graphene.Int(required=True)
        student_status = graphene.Int(required=True)

    application = graphene.Field(ApplicationType)

    def mutate(self, info, date_of_birth, source_of_referral, student_status):

        if not info.context.user.is_anonymous:

            new_app = Application(

                date_of_birth=date_of_birth,
                source_of_referral=source_of_referral,
                student_status=student_status,
                application_date=datetime.datetime.today()
            )

            new_app.save()

            this_user = VrUser.objects.get(user=info.context.user)
            this_user.application = new_app
            this_user.save()

            return CreateApplication(

                application=new_app
            )

        else:
            raise Exception("User not authenticated.")
