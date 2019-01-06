from django.db import models
from open_vr_api.models.employment import Employment
from open_vr_api.models.support import Support
from open_vr_api.models.medical_insurance_coverage import MedicalInsuranceCoverage


class Exit(models.Model):

    during_after_trial_work_experience = 1
    prior_order_of_selection = 2
    prior_signed_IPE = 3
    without_employment_outcome = 4
    noncompetitive_nonintegrated_employment = 5
    integrated_supported_employment = 6
    prior_to_eligibility_determination = 0

    exit_type_choices = (

        (during_after_trial_work_experience, 'Individual exited during or after a trial work experience.'),
        (prior_order_of_selection, 'Individual exited after eligibility, but from an order of selection waiting list.'),
        (prior_signed_IPE, 'Individual exited after eligibility, but prior to a signed IPE.'),
        (without_employment_outcome, 'Individual exited after an IPE without an employment outcome.'),
        (noncompetitive_nonintegrated_employment, 'Individual exited after an IPE in noncompetitive and/or nonintegrated employment.'),
        (integrated_supported_employment, 'Individual exited after an IPE in competitive and integrated employment or supported employment.'),
        (prior_to_eligibility_determination, 'Individual exited as an applicant, prior to eligibility determination or trial work.')

    )

    institutionalized = 1
    health_medical = 2
    death_of_individual = 3
    reserve_active_duty = 4
    foster_care = 5
    ineligible = 6
    criminal_offender = 7
    no_disabling_condition = 8
    no_impediment_employment = 9
    does_not_require_VR = 10
    disability_too_significant = 11
    no_long_term_service_available = 12
    transferred_to_another_agency = 13
    competitive_integrated_employment = 14
    extended_employment = 15
    extended_services_not_available = 16
    unable_to_locate_contact = 17
    no_longer_interested = 18
    no_longer_available_institutional = 19
    all_other_reasons = 20

    reason_choices = (

                         (institutionalized, 'Institutionalized'),
                         (health_medical, 'Health/Medical'),
                         (death_of_individual, 'Death of Individual'),
                         (reserve_active_duty, 'Reserve Forces Called to Active Duty'),
                         (foster_care, 'Foster Care'),
                         (ineligible, 'Ineligible'),
                         (criminal_offender, 'Criminal Offender'),
                         (no_disabling_condition, 'No Disabling Condition'),
                         (no_impediment_employment, 'No Impediment to Employment'),
                         (does_not_require_VR, 'Does Not Require VR Service'),
                         (disability_too_significant, 'Disability Too Significant to Benefit from Services'),
                         (no_long_term_service_available, 'No Long Term Source of Extended Services Available'),
                         (transferred_to_another_agency, 'Transferred to Another Agency'),
                         (competitive_integrated_employment, 'Achieved Competitive Integrated Employment Outcome'),
                         (extended_employment, 'Extended Employment'),
                         (extended_services_not_available, 'Extended Services Not Available'),
                         (unable_to_locate_contact, 'Unable to Locate or Contact'),
                         (no_longer_interested, 'No Longer Interested in Receiving Services or Further Services'),
                         (no_longer_available_institutional, 'Individual is No Longer Available for Services Due to Residence in an Institutional Setting Other Than a Prison or Jail'),
                         (all_other_reasons, 'All Other Reasons')
    )

    date = models.DateField()
    exit_type = models.IntegerField(choices=exit_type_choices)
    reason = models.IntegerField(choices=reason_choices)
    employment = models.OneToOneField(Employment, on_delete=models.PROTECT)
    support = models.OneToOneField(Support, on_delete=models.PROTECT)
    medical_insurance = models.OneToOneField(MedicalInsuranceCoverage, on_delete=models.PROTECT)
