from django.db import models


class IpeEmployment(models.Model):
    competitive_integrated_employment = 1
    self_employment = 2
    business_enterprise_program = 3
    state_based_BEP = 4
    extended_employment = 5
    employed_with_criteria = 6
    student_in_secondary = 7
    all_other_students = 8
    trainee_intern_volunteer = 9
    not_employed_other = 10

    employment_choices = (

        (competitive_integrated_employment, 'Competitive Integrated Employment'),
        (self_employment, 'Self-Employment'),
        (business_enterprise_program, 'Business Enterprise Program (BEP)'),
        (state_based_BEP, 'Employed: State Agency-managed Business Enterprise Program (BEP)'),
        (extended_employment, 'Employed: Extended Employment'),
        (employed_with_criteria, 'Employed: Meets One of the Following Criteria'),
        (student_in_secondary, 'Not Employed: Student in Secondary Education'),
        (all_other_students, 'Not Employed: All Other Students'),
        (trainee_intern_volunteer, 'Not Employed: Trainee, Intern or Volunteer'),
        (not_employed_other, 'Not Employed: Other')

    )

    employment = models.IntegerField(choices=employment_choices)
    primary_occupation = models.CharField(max_length=6)
    hourly_wage = models.DecimalField(decimal_places=2, max_digits=5)
    hours_worked_per_week = models.IntegerField()
    date_other_diploma = models.DateField(null=True)

