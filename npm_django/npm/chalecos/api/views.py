from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from chalecos.models import Chalecos
from chalecos.api.serializers import ChalecosSerializer

class ChalecosApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ChalecosSerializer
    queryset = Chalecos.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class ChalecosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ChalecosSerializer(request.user)
        return Response(serializer.data)
