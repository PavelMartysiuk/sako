from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from main.models import Contacts

from main.api.v1.serializers.contacts import ContactsSerializer


class ContactsView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
