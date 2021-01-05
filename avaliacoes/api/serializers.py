from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao

        # Usar tupla, lista ou string "__all__" para todos os campos
        fields: str = "__all__"
