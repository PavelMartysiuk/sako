from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters

from django_filters.rest_framework import DjangoFilterBackend

from core.paginators.base_paginator import BasePagination

from main.models import Manufacturer

from main.api.v1.serializers.manufactor import ManufactorSerializer


class ManufactorView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Manufacturer.objects.all()
    pagination_class = BasePagination
    # filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    #  search_fields = ('first_name', 'last_name',)
    # filterset_class = EmployeeFilter

    serializer_class = ManufactorSerializer
