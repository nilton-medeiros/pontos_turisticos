from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    Substituindo o queryset pelo método get_queryset() com uso de filtro (possibilidade de multiplos filtros)
    Implementar em urls.py o basename: router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
    E adicionar em core.serializers.py o campo aprovado na tupla se não estiver usando a string '__all__'
    """
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    # Sobrescrevendo o método get_queryset da classe ViewSet:
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
