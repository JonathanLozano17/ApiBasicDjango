from rest_framework import serializers
from usuarios.models import Usuarios

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'nombreUsuario', 'password', 'is_active', 'is_admin']