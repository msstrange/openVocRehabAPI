from django.db import models


class Disability(models.Model):
    # has_disabilty values
    has = 1
    has_not = 0
    did_not_self_identify = 9

    significantly_disabled = 1
    most_significantly_disabled = 2
    no_significant_disability = 0

    disability_choices = (

        (has, """Individual indicates that he/she has any "disability”, as defined in section 3(2)(a) of the Americans with Disabilities Act of 1990 (42 U.S.C. 12102).Under that definition, a "disability" is a physical or mental impairment that substantially limits one or more of the person's major life activities."""),
        (has_not, """Individual indicates that he/she does not have a disability that meets the definition"""),
        (did_not_self_identify, """Individual did not self-identify""")

    )

    significance_choices = (

        (significantly_disabled, 'Individual has a significant disability'),
        (most_significantly_disabled, 'Individual is most significantly disabled'),
        (no_significant_disability, 'Individual has no significant disability')

    )

    has_disability = models.IntegerField(choices=disability_choices)
    significance = models.IntegerField(choices=significance_choices)

