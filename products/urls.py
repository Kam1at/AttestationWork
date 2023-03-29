from rest_framework.routers import SimpleRouter
from products.apps import ProductsConfig
from products.views import ProductModelViewSet


app_name = ProductsConfig.name
router = SimpleRouter()
router.register(r'products', ProductModelViewSet, basename='products')
urlpatterns = router.urls
