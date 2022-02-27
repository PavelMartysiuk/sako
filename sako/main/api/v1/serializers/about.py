from rest_framework import serializers

from main.models import About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
