from rest_framework import serializers
from beneficiarios.models import Beneficiarios

class BeneficiariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiarios
        fields = '__all__'
