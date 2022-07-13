from rest_framework import routers
from offers.models import userdetails
from offers.models import Customer

from offers.viewsets import UserdetailsViewSet
from offers.viewsets import CustomerDetailsViewSet

router = routers.DefaultRouter()
router.register('userdetails',UserdetailsViewSet)
router.register('Customer',CustomerDetailsViewSet)