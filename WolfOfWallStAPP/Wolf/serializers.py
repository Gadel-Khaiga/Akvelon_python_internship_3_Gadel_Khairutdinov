from rest_framework import serializers
from .models import Wolf

class WolfListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wolf
        fields = '__all__'


class WolfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wolf
        fields = '__all__'