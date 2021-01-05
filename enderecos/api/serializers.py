from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco

        # Usar tupla, lista ou string "__all__" para todos os campos
        fields: str = "__all__"
