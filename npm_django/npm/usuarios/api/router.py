from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView)


from usuarios.api.views import UserApiViewSet, UserView


router_user = DefaultRouter()

#Api model user
router_user.register(
    prefix = 'users', basename='users', viewset=UserApiViewSet
)

#api model view
urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view())
]