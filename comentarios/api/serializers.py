from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario

        # Usar tupla, lista ou string "__all__" para todos os campos
        fields: str = "__all__"
