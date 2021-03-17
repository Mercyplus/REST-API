from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register(r'Customer', CustomerViewSet)
router.register(r'Category', CategoryViewSet)
router.register(r'Product', ProductViewSet)


urlpatterns = router.urls
