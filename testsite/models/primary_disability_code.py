from django.db import models
from testsite.models.disability import Disability


class PrimaryDisabilityCode(models.Model):
    no_impairment = '0'

    blindness = '1'
    other_visual_impairments = '2'
    deafness_primary_communication_visual = '3'
    deafness_primary_communication_auditory = '4'
    hearing_loss_primary_communication_visual = '5'
    hearing_loss_primary_communication_auditory = '6'
    other_hearing_impairments = '7'
    deaf_blindness = '8'
    communicative_impairments = '9'

    mobility_orthopedic_neurological = '10'
    manipulation_dexterity_orthopedic_neurological = '11'
    both_mobility_and_manipulation = '12'
    other_orthopedic = '13'
    respiratory = '14'
    general_physical_debilitation = '15'
    other_physical = '16'

    cognitive = '17'
    psychosocial = '18'
    other_mental = '19'

    cause_unknown = '0'
    accident_injury = '1'
    alcohol_abuse_dependence = '2'
    amputations = '3'
    anxiety_disorders = '4'
    arthritis_rheumatism = '5'
    asthma_other_allergies = '6'
    adhd = '7'
    autism = '8'
    blood_disorders = '9'
    cancer = '10'
    cardiac_circulatory_conditions = '11'
    cerebral_palsy = '12'
    congenital_condition_injury = '13'
    cystric_fibrosis = '14'
    depressive_other_mood = '15'
    diabetes_mellitus = '16'
    digestive = '17'
    drug_abuse_dependence = '18'
    eating_disorders = '19'
    end_stage_renal = '20'
    epilepsy = '21'
    HIV_AIDS = '22'
    immune_deficiencies = '23'
    mental_illness = '24'
    mental_retardation = '25'
    multiple_sclerosis = '26'
    muscular_dystrophy = '27'
    parkinsons_disease_neurological = '28'
    personality_disorders = '29'
    physical_disorders_conditions = '30'
    polio = '31'
    respiratory_disorders_other = '32'
    schizophrenia_other_psychotic = '33'
    specific_learning_disabilities = '34'
    spinal_chord_injury = '35'
    stroke = '36'
    traumatic_brain_injury = '37'

    type_of_impairment_choices = (

        (no_impairment, 'No Impairment'),
        (blindness, 'Blindness'),
        (other_visual_impairments, 'Other Visual Impairments'),
        (deafness_primary_communication_visual, 'Deafness, Primary Communication Visual'),
        (deafness_primary_communication_auditory, 'Deafness, Primary Communication Auditory'),
        (hearing_loss_primary_communication_visual, 'Hearing Loss, Primary Communication Visual'),
        (hearing_loss_primary_communication_auditory, 'Hearing Loss, Primary Communication Auditory'),
        (other_hearing_impairments, "Other Hearing Impairments (Tinnitus, Meniere's Disease, hyperacusis, etc."),
        (deaf_blindness, "Deaf-Blindness"),
        (communicative_impairments, 'Communicative Impairments (expressive/receptive)'),
        (mobility_orthopedic_neurological, 'Mobility Othopedic/Neurological Impairments'),
        (manipulation_dexterity_orthopedic_neurological, 'Manipulation/Dexterity Orthopedic/Neurological Impairments'),
        (both_mobility_and_manipulation, 'Respiratory Impairments'),
        (other_orthopedic, 'Other Orthopedic Impairments (e.g., limited range of motion'),
        (respiratory, 'Respiratory Impairments'),
        (general_physical_debilitation, 'General Physical Debilitation (e.g., fatigue, weakness, pain, etc.)'),
        (other_physical, 'Other Physical Impairments (not listed above)'),
        (cognitive,
         'Cognitive Impairments (e.g., impairments involving learning, thinking, processing information and concentration)'),
        (psychosocial, 'Psychosocial Impairments (e.g., interpersonal and behavioral impairments, difficulty coping)'),
        (other_mental, 'Other Mental Impairments')
    )

    source_of_impairment_choices = (

        (cause_unknown, 'Cause Unknown'),
        (accident_injury, 'Accident/Injury (Other than TBI or SCI)'),
        (alcohol_abuse_dependence, 'Alcohol Abuse or Dependence'),
        (amputations, 'Amputations'),
        (anxiety_disorders, 'Anxiety Disorders'),
        (arthritis_rheumatism, 'Arthritis and Rheumatism'),
        (asthma_other_allergies, 'Asthma and Other Allergies'),
        (adhd, 'Attention-Deficit Hyperactivity Disorder (ADHD)'),
        (autism, 'Autism'),
        (blood_disorders, 'Blood Disorders'),
        (cancer, 'Cancer'),
        (cardiac_circulatory_conditions, 'Cardiac and Other Conditions of the Circulatory System'),
        (cerebral_palsy, 'Cerebal Palsy'),
        (congenital_condition_injury, 'Congental Condition or Birth Injury'),
        (cystric_fibrosis, 'Cystic Fibrosis'),
        (depressive_other_mood, 'Depressive and Other Mood Disorders'),
        (diabetes_mellitus, 'Diabetes Mellitus'),
        (digestive, 'Digestive'),
        (drug_abuse_dependence, 'Drug Abuse or Dependence (other than alcohol)'),
        (eating_disorders, 'Eating Disorders (e.g., anorexia, bulimia, or complusive overeating)'),
        (end_stage_renal, 'End-Stage Renal Disease and Other Genitourinary System Disorders'),
        (epilepsy, 'Epilepsy'),
        (HIV_AIDS, 'HIV and AIDS'),
        (immune_deficiencies, 'Immune Deficiencies Excluding HIV/AIDS'),
        (mental_illness, 'Mental Illness (not listed elsewhere)'),
        (mental_retardation, 'Mental Retardation'),
        (multiple_sclerosis, 'Multiple Sclerosis'),
        (muscular_dystrophy, 'Muscular Dystrophy'),
        (parkinsons_disease_neurological, "Parkinson's Disease and Other Neurological Disorders"),
        (personality_disorders, 'Personality Disorders'),
        (physical_disorders_conditions, 'Physical Disorders/Conditions (not listed elsewhere)'),
        (polio, 'Polio'),
        (respiratory_disorders_other, 'Respiratory Disorders Other than Cystic Fibrosis or Asthma'),
        (schizophrenia_other_psychotic, 'Schizophrenia and Other Psychotic Disorders'),
        (specific_learning_disabilities, 'Specific Learning Disabilities'),
        (spinal_chord_injury, 'Spinal Chord Injury (SCI)'),
        (stroke, 'Stroke'),
        (traumatic_brain_injury, 'Traumatic Brain Injury (TBI)')

    )

    type_of_impairment = models.CharField(max_length=2, choices=type_of_impairment_choices)
    source_of_impairment = models.CharField(max_length=2, choices=source_of_impairment_choices)
