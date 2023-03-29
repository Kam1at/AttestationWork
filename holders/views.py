from rest_framework.viewsets import ModelViewSet

from holders.models import Holders
from holders.serializers import HoldersSerializer
from users.permissions import ActiveUser


class HoldersModelViewSet(ModelViewSet):
    """Контроллер для работы с сетями"""
    queryset = Holders.objects.all()
    serializer_class = HoldersSerializer
    filterset_fields = ["contacts__country"]
    permission_classes = [ActiveUser]
