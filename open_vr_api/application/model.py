from django.db import models
from open_vr_api.models.individual_characterists import IndividualCharacteristics
from open_vr_api.models.location_information import LocationInformation
from open_vr_api.models.support import Support
from open_vr_api.models.medical_insurance_coverage import MedicalInsuranceCoverage


class Application(models.Model):

    Cetificate_14c_Holders = 1
    Adult_Education_Literacy = 2
    American_Indian_VR = 3
    Independent_Living_Center = 4
    Child_Protective_Services = 5
    Community_Rehabilitation = 6
    Consumer_Organization = 7
    Department_Of_Labor = 8
    Primary_Secondary_Institution = 9
    Postsecondary_Institution = 10
    Employers = 11
    Extended_Employment_Providers = 11
    Faith_Based_Organizations = 13
    Family_Friends = 14
    Intellectual_Disability_Providers = 15
    Medical_Health_Provider = 16
    Mental_Health_Provider = 17
    Public_Housing_Authority = 18
    Self_Referral = 19
    Social_Security_Admin = 20
    Dept_Correction = 21
    TANF = 22
    VA_Benefits_Admin = 23
    VA_Health_Admin = 24
    Wagner_Peyser = 25
    Welfare = 26
    Workers_Comp = 27
    Other_One_Stop = 28
    Other = 29
    Other_State_Agency = 30
    Other_VR_State_Agency = 31
    Other_WIOA = 32

    Referral_Choices = (

        (Cetificate_14c_Holders, "14(c) Certificate Holders"),
        (Adult_Education_Literacy, "Adult Education and Literacy Programs"),
        (American_Indian_VR, "American Indian VR Services Program"),
        (Independent_Living_Center, "Centers for Independent Living"),
        (Child_Protective_Services, "Child Protective Services"),
        (Community_Rehabilitation, "Community Rehabilitation Programs"),
        (Consumer_Organization, "Consumer Organizations or Advocacy Groups"),
        (Department_Of_Labor, "Department of Labor Employment and Training Service Programs for Adults"
         + ", Dislocated Workers, and Youth"),
        (Primary_Secondary_Institution, "Educational Institutions (Elementary/Secondary)"),
        (Postsecondary_Institution, "Educational Institutions (Postsecondary)"),
        (Employers, "Employers"),
        (Extended_Employment_Providers, "Extended Employment Providers"),
        (Faith_Based_Organizations, "Faith Based Organizations"),
        (Family_Friends, "Family/Friends"),
        (Intellectual_Disability_Providers, "Intellectual and Developmental Disabilities Providers"),
        (Medical_Health_Provider, "Medical Health Provider (Public or Private)"),
        (Mental_Health_Provider, "Mental Health Provider (Public or Private)"),
        (Public_Housing_Authority, "Public Housing Authority"),
        (Self_Referral, "Self-referral"),
        (Social_Security_Admin, "Social Security Administration (Disability Determination Service or District office)"),
        (Dept_Correction, "State Department of Correction/Juvenile Justice"),
        (TANF, "Temporary Assistance for Needy Families (TANF)"),
        (VA_Benefits_Admin, "Veteran's Benefits Administration (which includes VA Vocational Rehabilitation)"),
        (VA_Health_Admin, "Veteran's Health Administration (the VA hospital system" +
         ", as well as the VA transitional living, transitional employment, and compensated work therapy programs)"),
        (Wagner_Peyser, "Wagner-Peyser Employment Service Program"),
        (Welfare, "Welfare Agency (State or local government)"),
        (Workers_Comp, "Worker's Compensation"),
        (Other_One_Stop, "Other One-stop Partner"),
        (Other, "Other Sources"),
        (Other_State_Agency, "Other State Agencies"),
        (Other_VR_State_Agency, "Other VR State Agencies"),
        (Other_WIOA, "Other WIOA-funded Programs including Job Corps, YouthBuild," +
         " Indian and Native Americans, and Migrant and Seasonal Farm-worker Programs")

    )

    Accommodation_504 = 1
    Individualized_Education_Program = 2
    No_Accommodation = 3
    Not_Student = 0

    Student_Status_Choice = (

        (Accommodation_504, "Individual is a student with a disability and has a section 504 accommodation."),
        (Individualized_Education_Program, "Individual is a student with adisability and" +
         " is receiving transition services under an Individualized Education Program (IEP)."),
        (No_Accommodation, "Individual is a student with a disability who does not have a section 504 accommodation"
         + " and is not receiving services under an IEP."),
        (Not_Student, "Individual is not a student with a disability.")

    )

    application_date = models.DateTimeField()
    date_of_birth = models.DateTimeField()
    individual_characteristics = models.OneToOneField(
        IndividualCharacteristics,
        on_delete=models.PROTECT,
        null=True
    )
    source_of_referral = models.IntegerField(choices=Referral_Choices)
    student_status = models.IntegerField(choices=Student_Status_Choice)
    location_information = models.OneToOneField(
        LocationInformation,
        on_delete=models.PROTECT,
        null=True
    )
    support = models.OneToOneField(
        Support,
        on_delete=models.PROTECT,
        null=True
    )
    medical_insurance_coverage = models.OneToOneField(
        MedicalInsuranceCoverage,
        on_delete=models.PROTECT,
        null=True
    )
