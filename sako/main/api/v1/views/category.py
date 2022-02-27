from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from main.models import Category

from main.api.v1.serializers.category import CategorySerializer


class CategoryView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
