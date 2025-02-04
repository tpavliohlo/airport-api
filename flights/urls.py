from django.urls import path, include
from rest_framework import routers

from flights.views import FlightViewSet, AirplaneViewSet, AirplaneTypesViewSet

router = routers.DefaultRouter()
router.register("flights", FlightViewSet)
router.register("airplanes", AirplaneViewSet)
router.register("airplane-types", AirplaneTypesViewSet)
urlpatterns = [path("", include(router.urls))]

app_name = "flight"
