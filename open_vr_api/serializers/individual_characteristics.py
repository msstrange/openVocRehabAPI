from rest_framework import serializers
from open_vr_api.models.individual_characterists import IndividualCharacteristics
from open_vr_api.application.model import Application
import datetime


class IndividualCharacteristicsSerializer(serializers.Serializer):

    sex = serializers.IntegerField()
    alaskan_native = serializers.IntegerField()
    asian = serializers.IntegerField()
    black = serializers.IntegerField()
    native_hawaiian = serializers.IntegerField()
    white = serializers.IntegerField()
    hispanic = serializers.IntegerField()
    veteran = serializers.BooleanField()

    def create(self, validated_data):

        ind_char = IndividualCharacteristics.objects.create(**validated_data)
        application = Application(
            individual_characteristics=ind_char, application_date=str(datetime.date.today()))
        application.save()
        return ind_char
