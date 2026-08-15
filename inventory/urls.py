from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CustomerViewSet, ProductViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('customers', CustomerViewSet)

urlpatterns = router.urls

