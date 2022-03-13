from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters

from django_filters.rest_framework import DjangoFilterBackend

from core.paginators.base_paginator import BasePagination

from main.models import Product

from main.api.v1.serializers.product import ProductListSerializer, ProductDetailSerializer
from main.api.v1.filters.product import ProductFilter


class ProductView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    pagination_class = BasePagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)

    filterset_class = ProductFilter

    default_serializer_class = ProductListSerializer

    serializer_classes = {
        'list': ProductListSerializer,
        'retrieve': ProductDetailSerializer,
    }

    def get_queryset(self):
        if self.action == 'retrieve':
            return Product.objects.prefetch_related('product_logo')
        elif self.action == 'list':
            return Product.objects.select_related('manufactor')
        return Product.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
