from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rujak.views import PembeliViewSet, RujakViewSet, BahanRujakViewSet

router = DefaultRouter()
router.register(r'pembeli', PembeliViewSet)
router.register(r'rujak', RujakViewSet)
router.register(r'bahan-rujak', BahanRujakViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
