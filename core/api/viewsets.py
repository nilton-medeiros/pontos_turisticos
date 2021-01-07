from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    Substituindo o queryset pelo método get_queryset() com uso de filtro (possibilidade de multiplos filtros)
    Implementar em urls.py o basename: router.register(r'pontoturistico', PontoTuristicoViewSet,
    basename='PontoTuristico')
    E adicionar em core.serializers.py o campo aprovado na tupla se não estiver usando a string '__all__'
    """
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    # Sobrescrevendo o método get_queryset da classe ViewSet (personalizando o filtro):
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['post'], detail=True)
    def enviar(self, request, pk=None):
        # Passar a chave: http://.../pontosturisticos/[pk-chave]/enviar/
        # Exemplo: http://.../pontosturisticos/1221255444587789258/enviar/
        pass
