from rest_framework import serializers
from .models import Pembeli, Rujak, BahanRujak

class PembeliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembeli
        fields = '__all__'

class RujakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rujak
        fields = '__all__'

class BahanRujakSerializer(serializers.ModelSerializer):
    class Meta:
        model = BahanRujak
        fields = '__all__'
