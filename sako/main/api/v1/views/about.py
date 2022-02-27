from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from main.models import About

from main.api.v1.serializers.about import AboutSerializer


class AboutView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
