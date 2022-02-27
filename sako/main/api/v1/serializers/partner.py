from rest_framework import serializers

from main.models import Partner



class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
