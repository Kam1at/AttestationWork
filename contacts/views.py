from rest_framework.viewsets import ModelViewSet
from contacts.models import Contacts
from contacts.serializers import ContactSerializer
from users.permissions import ActiveUser


class ContactsModelViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [ActiveUser]
