from rest_framework.viewsets import ModelViewSet
from products.models import Products
from products.serializers import ProductsSerializer
from users.permissions import ActiveUser


class ProductModelViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [ActiveUser]