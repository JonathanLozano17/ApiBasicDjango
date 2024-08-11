from rest_framework import serializers
from chalecos.models import Chalecos

class ChalecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chalecos
        fields = '__all__'
