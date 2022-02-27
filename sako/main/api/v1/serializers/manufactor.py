from rest_framework import serializers

from main.models import Manufacturer


class ManufactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'
