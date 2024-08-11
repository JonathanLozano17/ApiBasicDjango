from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from beneficiarios.api.views import BeneficiariosApiViewSet, BeneficiariosView, BeneficiariosByNombreView
from beneficiarios.api.BeneficiariosByCedulaView import BeneficiariosByCedulaView
router_beneficiarios = DefaultRouter()

# Registrar el ViewSet de Beneficiarios
router_beneficiarios.register(
    prefix='beneficiarios', basename='beneficiarios', viewset=BeneficiariosApiViewSet
)

# Registrar rutas
urlpatterns = [
    path('auth/me/', BeneficiariosView.as_view()),
    path('beneficiarios/cedula/<int:cedula>/', BeneficiariosByCedulaView.as_view(), name='beneficiarios_by_cedula'),
    path('beneficiarios/nombre/<str:nombre>/', BeneficiariosByNombreView.as_view(), name='beneficiarios_by_nombre'),
]

# Añadir las rutas generadas por el router
urlpatterns += router_beneficiarios.urls
