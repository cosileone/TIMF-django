from django.urls import include, path
from rest_framework import routers
from items.api.views import ItemViewSet
from realms.api.views import RealmViewSet

router = routers.SimpleRouter()
router.register(r'items', ItemViewSet, 'items')
router.register(r'realms', RealmViewSet, 'realms')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
