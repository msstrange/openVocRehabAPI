import graphene
from open_vr_api.user.model import VrUser
from .model import Application
import datetime


class CreateApplication(graphene.Mutation):

    success = graphene.Boolean()
    date_of_birth = graphene.Date()
    source_of_referral = graphene.Int()
    student_status = graphene.Int()
    application_date = graphene.Date()

    class Arguments:
        date_of_birth = graphene.Date()
        source_of_referral = graphene.Int()
        student_status = graphene.Int()

    def mutate(self, info, date_of_birth, source_of_referral, student_status):

        print(info.context.user.is_anonymous)

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

                success=True,
                date_of_birth=new_app.date_of_birth,
                source_of_referral=new_app.source_of_referral,
                student_status=new_app.student_status,
                application_date=new_app.application_date
            )

        else:
            return CreateApplication(success=False)
