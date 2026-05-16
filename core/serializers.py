from rest_framework import serializers
from .models import Genero, Filme

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class FilmeSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer(read_only=True)
    genero_id = serializers.PrimaryKeyRelatedField(queryset=Genero.objects.all(),source='genero', write_only=True)
    class Meta:
        model = Filme

        fields = ['id', 'titulo', 'sinopse', 'ano_lancamento','nota','disponivel','criado_em','genero','genero_id']