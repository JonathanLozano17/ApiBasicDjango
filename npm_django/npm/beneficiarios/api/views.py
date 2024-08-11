from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status

from beneficiarios.models import Beneficiarios
from beneficiarios.api.serializers import BeneficiariosSerializer

class BeneficiariosApiViewSet(ModelViewSet):
    serializer_class = BeneficiariosSerializer
    queryset = Beneficiarios.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar por cedula
        cedula = self.request.query_params.get('cedula')
        if cedula is not None:
            queryset = queryset.filter(cedula=cedula)

        # Filtrar por nombre
        nombre = self.request.query_params.get('nombre')
        if nombre is not None:
            queryset = queryset.filter(nombre__icontains=nombre)

        return queryset

class BeneficiariosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = BeneficiariosSerializer(request.user)
        return Response(serializer.data)
    



class BeneficiariosByNombreView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, nombre):
        beneficiarios = Beneficiarios.objects.filter(nombre__icontains=nombre)
        serializer = BeneficiariosSerializer(beneficiarios, many=True)
        return Response(serializer.data)
    


