from django.db import models


class Employment(models.Model):

    competitive_integrated_employment = 1
    self_employment = 2
    business_enterprise_program =3
    supported_employment = 4
    supported_short_term = 5
    uncompensated_employment = 6
    termination_notice = 7

    outcome_choices = (

        (competitive_integrated_employment, 'Competitive Integrated Employment'),
        (self_employment, 'Self-Employment'),
        (business_enterprise_program, 'Business Enterprise Program (BEP)'),
        (supported_employment, 'Supported Employment in Competitive Integrated Employment'),
        (supported_short_term, 'Supported Employment on Short-term Basis'),
        (uncompensated_employment, 'Uncompensated Employment'),
        (termination_notice, 'Termination Notice, WARN,or Transitioning Service Member')
    )

    outcome = models.IntegerField(choices=outcome_choices)
    primary_occupation_outcome = models.CharField(max_length=6)
    start_date_employment = models.DateField()
    hourly_wage = models.DecimalField(max_digits=5, decimal_places=2)
    hours_worked_per_week = models.IntegerField()
