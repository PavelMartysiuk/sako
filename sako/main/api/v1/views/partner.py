from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from main.models import Partner

from main.api.v1.serializers.partner import PartnerSerializer


from core.paginators.base_paginator import BasePagination


class PartnerView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = BasePagination

