from rest_framework import serializers
from .models import Pembeli, Rujak, BahanRujak

class PembeliSerializer(serializers.ModelSerializer):
    model = Pembeli
    class Meta:
        fields = ['nama', 'alamat', 'nomor_telepon']

class RujakSerializer(serializers.ModelSerializer):
    model = Rujak
    class Meta:
        fields = ['nama', 'harga']

class BahanRujakSerializer(serializers.ModelSerializer):
    model = BahanRujak
    class Meta:
        fields = ['nama', 'jumlah']
