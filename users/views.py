from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.permissions import ActiveUser
from users.serializers import UsersSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [ActiveUser()]
