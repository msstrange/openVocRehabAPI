from django.db import models


class Support(models.Model):
    personal_income = 1
    family_and_friends = 2
    public_support = 3
    support_other_sources = 4

    Primary_Source_Choices = (

        (personal_income,
            "Applicant’s primary source of support is personal income "
            + "(employment earnings, interest, dividends, rent, or retirement including social security)"),

        (family_and_friends, "Applicant’s primary source of support is family and friends."),
        (public_support, "Applicant’s primary source of support is public support (SSI, SSDI, TANF, etc.)."),

        (support_other_sources, "Applicant’s primary source of support is from other sources "
            + "(e.g., private disability insurance and private charities)")

    )

    ssdi = models.BooleanField()
    ssi = models.BooleanField()
    tanf = models.BooleanField()
    general_assistance = models.BooleanField()
    veterans_disability = models.BooleanField()
    workers_compensation = models.BooleanField()
    unemployment_insurance = models.BooleanField()
    primary_source_support = models.IntegerField(choices=Primary_Source_Choices)


