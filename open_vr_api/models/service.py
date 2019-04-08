from django.db import models


class Service(models.Model):
    provided_in_house = 1
    no_longer_provided = 2

    provided_in_house_choices = (

        (provided_in_house, 'service was provided in whole or part by VR agency staff (in-house)'),
        (no_longer_provided, 'service was provided in whole or part by VR agency staff (in-house) and is no longer being provided. '),
        (None, 'service was not provided by VR agency staff (in-house).')
    )

    provided_VR_agency = 1

    provided_through_VR_agency_choices = (

        (provided_VR_agency, 'service was provided in whole or part through purchase by the VR agency.'),
        (no_longer_provided,
         'service was provided in whole or part through purchase by the VR agency and is no longer being provided.'),
        (None, 'service was not provided through purchase by VR agency.')

    )

    community_Rehabilitation_programs = 1
    private_CRP = 2
    public_service_provider = 3
    other_service_provider = 4

    purchased_service_provider_choices = (

        (community_Rehabilitation_programs, 'Community Rehabilitation Programs (CRPs)'),
        (private_CRP, 'Private CRP'),
        (public_service_provider, 'Public Service Provider'),
        (other_service_provider, 'Other Private Service Provider')

    )

    provided_by_comparable_services_benefits = 1

    comparable_services_and_benefits_choices = (

        (provided_by_comparable_services_benefits,
         'service was provided in whole or part by comparable services and benefits providers.'),
        (no_longer_provided,
         'service was provided in whole or part by comparable services and benefits and is no longer being provided.'),
        (None, 'service was not provided by comparable services and benefits providers.')

    )

    adult_education_literacy = 1
    dislocated_worker_dol = 2
    indian_vr_services = 3
    public_independent_living = 4
    child_protective_services = 5
    public_Rehabilitation_program = 6
    employer_provided_benefits = 7
    public_elementary_secondary = 8
    public_institution_postsecondary = 9
    public_employment_network = 10
    federal_student_aid = 11
    intellectual_developmental_disabilities = 12
    medical_health_provider = 13
    mental_health_provider = 14
    one_stop_partner = 15
    public_housing_authority = 16
    social_security_administration = 17
    state_correction_juvenile = 18
    state_employment_agency = 19
    veterans_benefits_administration = 20
    veterans_health_administration = 21
    wagner_peyser_employment = 22
    welfare_state_or_local = 23

    comparable_services_type_choices = (
        (adult_education_literacy, 'Adult education and Literacy program administered by the Department of Education'),
        (dislocated_worker_dol, 'Adult, Dislocated Worker and Youth program administered by Department of Labor (DOL)'),
        (indian_vr_services, 'American Indian VR Services Program'),
        (public_independent_living, 'Public Centers for Independent Living'),
        (child_protective_services, 'Child Protective Service'),
        (public_Rehabilitation_program, 'Public Rehabilitation Program'),
        (employer_provided_benefits, 'Employer Provided Benefits'),
        (public_elementary_secondary, 'Public Educational Institution (elementary/secondary)'),
        (public_institution_postsecondary, 'Public Educational Institution (postsecondary)'),
        (public_employment_network, 'Public Employment Network (not otherwise listed)'),
        (federal_student_aid, 'Federal Student Aid (e.g., Pell grants, Supplemental Educational Opportunity Grant, work study, etc.)'),
        (intellectual_developmental_disabilities, 'Intellectual and Developmental Disabilities Agency (Public)'),
        (medical_health_provider, 'Medical Health Provider (Public)'),
        (mental_health_provider, 'Mental Health Provider (Public)'),
        (one_stop_partner, 'One-stop Partner (not listed separately)'),
        (public_housing_authority, 'Public Housing Authority'),
        (social_security_administration, 'Social Security Administration (Disability Determination Service or District office)'),
        (state_correction_juvenile, 'State Department of Correction/Juvenile Justice'),
        (state_employment_agency, 'State Employment Service Agency'),
        (veterans_benefits_administration, "Veteran's Benefits Administration (which includes VA Vocational Rehabilitation)"),
        (veterans_health_administration, "Veteran's Health Administration (the VA hospital system, as well as the VA transitional living, transitional employment, and compensated work therapy programs)"),
        (wagner_peyser_employment, 'Wagner-Peyser Employment Service Program'),
        (welfare_state_or_local, 'Welfare Agency (State or local government)')

    )

    provided_in_house = models.IntegerField(null=True, choices=provided_in_house_choices)
    provided_through_VR_agency_choices = models.IntegerField(null=True, choices=provided_through_VR_agency_choices)
    purchased_service_provider = models.IntegerField(choices=purchased_service_provider_choices)
    expenditure_for_purchased_service = models.DecimalField(decimal_places=2, max_digits=5)
    SE_funds_expended = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    comparable_services_and_benefits = models.IntegerField(choices=comparable_services_and_benefits_choices)
    comparable_services_type = models.IntegerField(choices=comparable_services_type_choices)
