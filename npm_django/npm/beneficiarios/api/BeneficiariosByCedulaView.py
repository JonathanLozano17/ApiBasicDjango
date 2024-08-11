from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from beneficiarios.models import Beneficiarios
from beneficiarios.api.serializers import BeneficiariosSerializer

class BeneficiariosByCedulaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cedula):
        try:
            beneficiario = Beneficiarios.objects.get(cedula=cedula)
            serializer = BeneficiariosSerializer(beneficiario)
            return Response(serializer.data)
        except Beneficiarios.DoesNotExist:
            return Response({'error': 'Beneficiario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
