from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao

        # Usar tupla ou string "__all__" para todos os campos
        fields: str = "__all__"
