from rest_framework.routers import SimpleRouter
from contacts.apps import ContactsConfig
from contacts.views import ContactsModelViewSet


app_name = ContactsConfig.name
router = SimpleRouter()
router.register(r'contacts', ContactsModelViewSet, basename='contacts')
urlpatterns = router.urls
