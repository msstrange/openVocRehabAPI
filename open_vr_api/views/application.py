from open_vr_api.application.model import Application
from open_vr_api.serializers.application import ApplicationSerializer
from open_vr_api.user.model import VrUser
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import datetime


class ApplicationDetail(
        mixins.CreateModelMixin,
        generics.GenericAPIView):

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid()
        new_app = Application(
            date_of_birth=serializer.data.get("date_of_birth"),
            application_date=datetime.date.today(),
            source_of_referral=serializer.data.get("source_of_referral"),
            student_status=serializer.data.get("student_status"))
        new_app.save()
        new_vr_user, created = VrUser.objects.get_or_create(
            user=request.user, application=new_app)
        if created:
            new_vr_user.save()
        return Response(f'Response : application created successfully.')
