from django.urls import path, include
from rest_framework import routers

from flights.views import FlightViewSet, AirplaneViewSet

router = routers.DefaultRouter()
router.register("flights", FlightViewSet)
router.register("airplanes", AirplaneViewSet)
urlpatterns = [path("", include(router.urls))]

app_name = "flight"
