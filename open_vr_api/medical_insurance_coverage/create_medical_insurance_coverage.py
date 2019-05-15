import graphene
from open_vr_api.user.model import VrUser
from .model import MedicalInsuranceCoverage
from .type import MedicalInsuranceCoverageType


class CreateMedicalInsuranceCoverage(graphene.Mutation):

    class Arguments:
        medicaid_at_application = graphene.Boolean(required=True)
        medicare_at_application = graphene.Boolean(required=True)
        affordable_care_exchange = graphene.Boolean(required=True)
        public_insurance_from_other_source = graphene.Boolean(required=True)
        private_insurance_through_employer = graphene.Boolean(required=True)
        not_yet_eligible_for_private_insurance = graphene.Boolean(required=True)
        other_private_insurance = graphene.Boolean(required=True)

    medical_insurance_coverage = graphene.Field(MedicalInsuranceCoverageType)

    def mutate(self, info, postal_code, medicaid_at_application, medicare_at_application,
               affordable_care_exchange, public_insurance_from_other_source, private_insurance_through_employer, not_yet_eligible_for_private_insurance,
               other_private_insurance):

        if not info.context.user.is_anonymous:

            this_user = VrUser.objects.get(user=info.context.user)

            medical_insurance_coverage = MedicalInsuranceCoverage(

                medicaid_at_application=medicaid_at_application,
                medicare_at_application=medicare_at_application,
                affordable_care_exchange=affordable_care_exchange,
                public_insurance_from_other_source=public_insurance_from_other_source,
                private_insurance_through_employer=private_insurance_through_employer,
                not_yet_eligible_for_private_insurance=not_yet_eligible_for_private_insurance,
                other_private_insurance=other_private_insurance

            )

            medical_insurance_coverage.save()

            this_user.application.medical_insurance_coverage = location_information

            this_user.application.medical_insurance_coverage.save()

            return CreateMedicalInsuranceCoverage(

                medical_insurance_coverage=medical_insurance_coverage

            )

        else:

            raise Exception("User not authenticated.")