from django.db import models
from open_vr_api.models.individualized_plan_for_employment import IndividualizedPlanForEmployment


class Education(models.Model):

    attending_elementary_school = 1
    alternative_course_of_study = 2
    attending_post_secondary = 3
    not_within_compulsory_attendance = 4
    has_secondary_diploma = 5
    has_not_received_diploma = 6

    school_status_choices = (

        (attending_elementary_school, 'Individual has not received a secondary school diploma or its recognized equivalent and is attending any elementary or secondary school (including elementary, intermediate, junior high school, whether full or part-time)'),
        (alternative_course_of_study, 'Individual has not received a secondary school diploma or its recognized equivalent and is attending an alternative secondary school or an alternative course of study approved by the local educational agency whether full or part-time.'),
        (attending_post_secondary, 'Individual has received a secondary school diploma or its recognized equivalent and is attending a postsecondary school or program (whether full or part-time), or is between school terms and is enrolled to return to school.'),
        (not_within_compulsory_attendance, 'Individual is not within the age of compulsory school attendance; and is no longer attending any school and has not received a secondary school diploma or its recognized equivalent.'),
        (has_secondary_diploma, 'Individual is not attending any school and has either a secondary school diploma or has attained a secondary school equivalency.'),
        (has_not_received_diploma, 'Individual is within the age of compulsory school attendance, but has not attended school for at least the most recent complete school year calendar quarter and has not received a secondary school diploma or its recognized equivalent.')

    )

    secondary_school_diploma = 1
    secondary_school_equivalency = 2
    certificate_of_attendance = 3
    one_or_more_post_secondary = 4
    post_secondary_certification_license = 5
    associates_degree = 6
    bachelors_degree = 7
    beyond_bachelors_degree = 8
    no_educational_level = 9

    highest_educational_level_choices = (

        (secondary_school_diploma, 'Individual attained a secondary school diploma.'),
        (secondary_school_equivalency, 'Individual attained a secondary school equivalency.'),
        (certificate_of_attendance, 'Individual has a disability and attained a certificate of attendance/completion as a result of successfully completing an Individualized Education Program (IEP).'),
        (one_or_more_post_secondary, 'Individual completed one or more years of postsecondary education.'),
        (post_secondary_certification_license, 'Individual attained a postsecondary certification, license, or educational certificate (non-degree).'),
        (associates_degree, 'Individual attained an Associate’s Degree'),
        (bachelors_degree, 'Individual attained a Bachelor’s Degree.'),
        (beyond_bachelors_degree, 'ndividual attained a degree beyond a Bachelor’s Degree.'),
        (no_educational_level, 'No educational level was completed.')

    )

    highest_level_freshman = 1
    highest_level_sophomore = 2
    highest_level_junior = 3
    highest_level_senor = 4
    not_enrolled_post_secondary = 0

    highest_post_secondary_year_choices = (

        (highest_level_freshman, 'Highest level of postsecondary education the individual is enrolled in is the first academic year (Freshman).'),
        (highest_level_sophomore, 'Highest level of postsecondary education the individual is enrolled in is the second academic year (Sophomore)'),
        (highest_level_junior, 'Highest level of postsecondary education the individual is enrolled in is the third academic year (Junior).'),
        (highest_level_senor, 'Highest level of postsecondary education the individual is enrolled in is the fourth academic year (Senior)'),
        (not_enrolled_post_secondary, 'Individual is not enrolled in postsecondary education.')

    )

    definition_students_with_disabilities = models.CharField(max_length=5)
    school_status = models.IntegerField(choices=school_status_choices)
    highest_educational_level = models.IntegerField(choices=highest_educational_level_choices)
    elementary_or_secondary_grade_completed = models.IntegerField()
    enrolled_in_secondary_education = models.BooleanField()
    date_received_certificate_of_completion = models.DateField(blank=True, null=True)
    enrolled_in_state_adult_secondary = models.BooleanField()
    attained_secondary_diploma = models.BooleanField()
    date_attained_ged = models.DateField(blank=True, null=True)
    highest_post_secondary_year = models.IntegerField(choices=highest_post_secondary_year_choices)
    enrolled_in_post_secondary = models.BooleanField()
    date_enrolled_education_or_training_program = models.DateField(null=True, blank=True)
    some_postsecondary = models.BooleanField()
    date_associate_degree = models.DateField(null=True)
    date_bachelors_degree = models.DateField(null=True)
    date_masters_degree = models.DateField(null=True)
    date_graduate_degree = models.DateField(null=True)
