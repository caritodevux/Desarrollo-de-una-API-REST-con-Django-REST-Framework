from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = [
            'id',
            'titulo',
            'descripcion',
            'completada',
            'fecha_creacion'
        ]
        read_only_fields = [
            'id',
            'fecha_creacion'
        ]
    def validate_titulo(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "El título debe contener al menos 3 caracteres."
            )
        return value