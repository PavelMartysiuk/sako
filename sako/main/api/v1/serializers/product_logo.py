from rest_framework import serializers

from main.models import ProductLogo



class ProductLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLogo
        fields = '__all__'
