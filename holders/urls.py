from rest_framework.routers import SimpleRouter
from holders.apps import HoldersConfig
from holders.views import HoldersModelViewSet


app_name = HoldersConfig.name
router = SimpleRouter()
router.register(r'', HoldersModelViewSet, basename='holders')
urlpatterns = router.urls
