from .models import Tarea
from rest_framework import serializers

class TareaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarea
        fields = ('nombre',)