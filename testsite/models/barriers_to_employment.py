from django.db import models


class BarriersToEmployment(models.Model):

    exhausting_lifetime_eligibility = 1
    not_exhausting_lifetime_eligibility = 0
    never_received_TANF = 9

    exhausting_TANF_choices = (

        (exhausting_lifetime_eligibility, 'Individual is within two years of exhausting lifetime eligibility under part A of Title IV of the Social Security Act (42 U.S.C. 601 et seq.)'),
        (not_exhausting_lifetime_eligibility, 'Individual does not meet the condition described above. '),
        (never_received_TANF, 'Individual has never received TANF or the individual has already exhausted lifetime TANF eligibility')

    )

    meets_ex_offender = 1
    not_ex_offender = 0
    does_not_self_identify = 9

    ex_offender_choices = (

        (meets_ex_offender, 'Individual meets the definition of an ex-offender.'),
        (not_ex_offender, 'Individual does not meet the definition of ex-offender.'),
        (does_not_self_identify, 'Individual did not self-identify')

    )

    individual_perceives = 1
    individual_does_not_perceive = 0

    cultural_barrier_choices = (

        (individual_perceives, 'Individual perceives himself or herself as possessing attitudes, beliefs, customs or practices that influence a way of thinking, acting or working that may serve as a hindrance to employment.'),
        (individual_does_not_perceive, 'Individual does not perceive himself or herself as possessing attitudes, beliefs, customs or practices that influence a way of thinking, acting or working that may serve as a hindrance to employment.'),
        (does_not_self_identify, 'Individual did not self-identify.')

    )

    is_single_parent = 1
    not_single_parent = 0

    single_parent_choices = (

        (is_single_parent, ''),
        (not_single_parent, ''),
        (does_not_self_identify, '')

    )

    primarily_employed_agriculture = 1
    seasonal_farmworker = 2
    dependent_of_seasonal_farmworker = 3
    not_seasonal_farmworker = 0

    migrant_seasonal_farmworker_choices = (

        (primarily_employed_agriculture, 'Individual is a low-income individual who for 12 consecutive months out of the 24 months prior to application for the program involved, has been primarily employed in agriculture or fish farming labor that is characterized by chronic unemployment or underemployment'),
        (seasonal_farmworker, 'Individual is a seasonal farmworker whose agricultural labor requires travel to a job site such that the farmworker is unable to return to a permanent place of residence within the same day.'),
        (dependent_of_seasonal_farmworker, 'Individual is a dependent (as defined in 20 CFR 685.110) of the individual described as a seasonal or migrant seasonal farmworker above.'),
        (not_seasonal_farmworker, 'Individual does not meet any of the migrant or seasonal farmworker conditions listed above.')

    )

    long_term_unemployed = models.BooleanField()
    exhausting_TANF = models.IntegerField(choices=exhausting_TANF_choices)
    foster_care_youth = models.BooleanField()
    homeless_individual_children = models.BooleanField()
    ex_offender = models.IntegerField(choices=ex_offender_choices)
    low_income = models.BooleanField()
    english_language_learner = models.BooleanField()
    basic_skills_deficient = models.BooleanField()
    cultural_barriers = models.IntegerField(choices=cultural_barrier_choices)
    single_parent = models.IntegerField(choices=single_parent_choices)
    displaced_homemaker = models.BooleanField()
    migrant_seasonal_farmworker = models.IntegerField(choices=migrant_seasonal_farmworker_choices)