from rest_framework import serializers


class ApplicationSerializer(serializers.Serializer):

    date_of_birth = serializers.DateField()
    source_of_referral = serializers.IntegerField()
    student_status = serializers.IntegerField()
