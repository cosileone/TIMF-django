from django.urls import include, path
from rest_framework import routers
from items.api import views

router = routers.SimpleRouter()
router.register(r'items', views.ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
