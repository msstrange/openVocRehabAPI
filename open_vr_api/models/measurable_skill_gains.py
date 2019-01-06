from django.db import models


class MeasurableSkillGains(models.Model):

    date_educational_functional_level = models.DateField(null=True)
    date_skill_gain_secondary = models.DateField(null=True)
    date_postsecondary_transcript = models.DateField(null=True)
    date_training_milestone = models.DateField(null=True)
    date_skill_progression = models.DateField(null=True)