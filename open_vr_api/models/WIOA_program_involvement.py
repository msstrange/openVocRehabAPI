from django.db import models


class WIOAProgramInvolvement(models.Model):

    adult_employment_training = 1
    statewide_workforce_investment = 2
    both = 3
    did_not_receive_services = 0

    did = 1
    did_not = 0
    unable_to_track = 9

    received_services_133b = 1
    received_services_133a = 2
    both_133a_133b = 3

    a_b_vocational_rehabilitation = 1
    department_veterans_affairs = 2
    both_vocational_rehabilitation = 3
    unknown = 9

    adult_choices = (

        (adult_employment_training, 'Individual received services under WIOA section 133(b)(2)(A) [Adult Employment and Training Activities] as an individual who is not less than age 18 at the time of program entry.'),
        (statewide_workforce_investment, 'Individual received services under WIOA section 133(a)(1) [Statewide Workforce Investment Activities].'),
        (both, 'Individual received services under WIOA sections 133(b)(2)(A) [Adult Employment and Training Activities] and 132(b)(1) [Statewide Workforce Investment Activities].'),
        (did_not_receive_services, 'Individual did not receive services under the WIOA sections listed above.')

    )

    adult_education_choices = (

        (did, 'Individual did receive Adult Education services.'),
        (did_not, 'Individual did not receive any Adult Education services.'),
        (unable_to_track, 'Unable to track enrollment in the program.')

    )

    dislocated_worker_choices = (

        (received_services_133b, 'Individual received services under section 133(b)(2)(B)'),
        (received_services_133a, 'Individual received services under section 133(a)of WIOA.'),
        (both_133a_133b, 'Individual received services under sections 133(b)(2)(B) and 133(a) of WIOA.'),
        (did_not_receive_services, 'Individual did not receive services under the WIOA sections listed above.')
    )

    job_corps_choices = (

        (did, 'Individual received services under WIOA title I Chapter 4, Subtitle C.'),
        (did_not, 'Individual did not receive services under WIOA title I Chapter 4, Subtitle C.'),
        (unable_to_track, 'Unable to track enrollment in program.')

    )

    vocational_rehabilitation_choices = (

        (a_b_vocational_rehabilitation, 'Individual received services under parts A and B of title I of the Rehabilitation Act of 1973'),
        (department_veterans_affairs, 'Individual received services from the Department of Veterans Affairs Vocational Rehabilitation and Employment'),
        (both_vocational_rehabilitation, 'Individual received services from both vocational rehabilitation programs listed above.'),
        (did_not_receive_services, 'Individual did not receive any services described above'),
        (unknown, 'Unknown')

    )

    wagner_peyser_choices = (

        (did, 'Individual received services under the Wagner-Peyser Act, as amended by title III of WIOA'),
        (did_not, 'Individual did not receive services under the Wagner-Peyser Act.'),
        (unable_to_track, 'Unable to track enrollment in program.')

    )

    received_128_b_WIOA = 1
    received_128_a_WIOA = 2
    receive_128_a_and_b = 3

    youth_choices = (

        (received_128_b_WIOA, 'Individual received services under section 128(b) of WIOA.'),
        (received_128_a_WIOA, 'Individual received services under section 128(a) of WIOA.'),
        (receive_128_a_and_b, 'Individual received services under sections 128(b) and 128(a) of WIOA.'),
        (did_not_receive_services, 'Individual did not receive services under the WIOA sections listed above.')

    )

    adult = models.IntegerField(choices=adult_choices)
    adult_education = models.IntegerField(choices=adult_education_choices)
    dislocated_worker = models.IntegerField(choices=dislocated_worker_choices)
    job_corps = models.IntegerField(choices=job_corps_choices)
    vocational_rehabilitation = models.IntegerField(choices=vocational_rehabilitation_choices)
    wagner_peyzer = models.IntegerField(choices=wagner_peyser_choices)
    youth = models.IntegerField(choices=youth_choices)
    youth_build = models.CharField(max_length=14, null=True)
