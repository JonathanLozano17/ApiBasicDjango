from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from chalecos.api.views import ChalecosApiViewSet, ChalecosView

router_chalecos = DefaultRouter()

# Registrar el ViewSet de Chalecos
router_chalecos.register(
    prefix='chalecos', basename='chalecos', viewset=ChalecosApiViewSet
)

# Registrar rutas
urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', ChalecosView.as_view())
]

# Añadir las rutas generadas por el router
urlpatterns += router_chalecos.urls
