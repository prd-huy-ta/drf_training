from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'products', views.ProductViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'unit', views.UnitViewSet)

router.register(r"customers", views.CustomerViewSet, basename="customers")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
