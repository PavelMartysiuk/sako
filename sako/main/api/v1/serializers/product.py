from rest_framework import serializers

from main.models import Product

from main.api.v1.serializers.product_logo import ProductLogoSerializer


class ProductDetailSerializer(serializers.ModelSerializer):
    product_logo = ProductLogoSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('main_logo', 'id', 'name')
