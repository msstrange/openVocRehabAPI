from django.db import models


class QuarterlyReport(models.Model):
    unsubsidized_employment = 1
    registered_apprenticeship = 2
    individual_in_military = 3
    competitive_integrated_employment = 4
    information_not_yet_available = 9
    not_employed = 0

    employment_choices = (

        (unsubsidized_employment,
         'ndividual is in unsubsidized employment, not including Registered Apprenticeship, the military, or competitive integrated employment under VR.'),
        (registered_apprenticeship, 'Individual is in a Registered Apprenticeship.'),
        (individual_in_military, 'Individual is in the military.'),
        (competitive_integrated_employment, 'ndividual is in competitive integrated employment (VR only).'),
        (information_not_yet_available, 'Individual has exited but employment information is not yet available.'),
        (not_employed, 'Individual not employed in the first quarter after exit quarter.')

    )

    ui_wage_data = 1
    federal_employment_records = 2
    military_employment_records = 3
    non_ui_wage_verification = 4
    match_information_not_yet_available = 5

    type_employment_match_choices = (

        (ui_wage_data, 'Method used in determining individual’s employment status was UI wage data.'),
        (federal_employment_records,
         'Method used in determining individual’s employment status was Federal employment records (e.g., OPM, USPS).'),
        (military_employment_records,
         'Method used in determining individual’s employment status was military employment records'),
        (non_ui_wage_verification,
         'Method used in determining individual’s employment status was non- UI wage verification.'),
        (match_information_not_yet_available, 'Information not yet available.'),
        (not_employed, 'Individual is not employed.')

    )

    employment = models.IntegerField(choices=employment_choices)
    type_employment_match = models.IntegerField(choices=type_employment_match_choices)
    wages = models.DecimalField(decimal_places=2, max_digits=5)
