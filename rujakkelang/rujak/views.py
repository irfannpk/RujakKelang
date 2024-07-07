from rest_framework import viewsets, serializers
from .models import Pembeli, Rujak, BahanRujak
from .serializers import PembeliSerializer, RujakSerializer, BahanRujakSerializer

class PembeliViewSet(viewsets.ModelViewSet):
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer

class RujakViewSet(viewsets.ModelViewSet):
    queryset = Rujak.objects.all()
    serializer_class = RujakSerializer

class BahanRujakViewSet(viewsets.ModelViewSet):
    queryset = BahanRujak.objects.all()
    serializer_class = BahanRujakSerializer
