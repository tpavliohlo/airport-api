from django.urls import path, include
from rest_framework import routers

from flights.views import FlightViewSet

router = routers.DefaultRouter()
router.register("flights", FlightViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "flight"
