from testsite.models.individual_characterists import IndividualCharacteristics
from testsite.serializers.individual_characteristics import IndividualCharacteristicsSerializer
from testsite.user.model import VrUser
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class IndividualCharacteristicsDetail(
        mixins.CreateModelMixin,
        generics.GenericAPIView):

    queryset = IndividualCharacteristics.objects.all()
    serializer_class = IndividualCharacteristicsSerializer
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        vr_user = VrUser.objects.filter(user=request.user.pk)
        serializer = IndividualCharacteristicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
