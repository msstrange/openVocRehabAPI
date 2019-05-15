from django.db import models


class IndividualCharacteristics(models.Model):
    Male = 1
    Female = 2
    Gender_Not_Identified = 9

    Gender_Choices = (
            (Male, 'Male'),
            (Female, 'Female'),
            (Gender_Not_Identified, 'Individual did not identify')
        )

    Is = 1
    Is_Not = 0
    Did_Not_Identify = 9

    Race_Choices = (

        (Is, 'Is'),
        (Is_Not, 'Is not'),
        (Did_Not_Identify, 'Individual did not identify')

    )

    private_residence = 1
    community_residential_facility = 2
    rehabilitation_facility = 3
    mental_health_facility = 4
    nursing_home = 5
    correctional_facility = 6
    halfway_house = 7
    substance_treatment_center = 8
    homeless_shelter = 9
    other = 10

    Living_Arrangement_Choices = (

        (private_residence, 'Private Residence (independent, or with family or other person)'),
        (community_residential_facility, 'Community Residential Facility/Group Home'),
        (rehabilitation_facility, 'Rehabilitation Facility'),
        (mental_health_facility, 'Mental Health Facility'),
        (nursing_home, 'Nursing Home'),
        (correctional_facility, 'Correctional Facility'),
        (halfway_house, 'Halfway House'),
        (substance_treatment_center, 'Substance Abuse Treatment Center'),
        (homeless_shelter, 'Homeless/Shelte'),
        (other, 'Other'),

    )

    sex = models.IntegerField(choices=Gender_Choices)
    alaskan_native = models.IntegerField(choices=Race_Choices)
    asian = models.IntegerField(choices=Race_Choices)
    black = models.IntegerField(choices=Race_Choices)
    native_hawaiian = models.IntegerField(choices=Race_Choices)
    white = models.IntegerField(choices=Race_Choices)
    hispanic = models.IntegerField(choices=Race_Choices)
    veteran = models.BooleanField()
    living_arrangement = models.IntegerField(choices=Living_Arrangement_Choices)



