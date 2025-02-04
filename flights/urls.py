from django.urls import path, include
from rest_framework import routers

from flights.views import FlightViewSet, AirplaneViewSet, AirplaneTypesViewSet, TicketViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register("flights", FlightViewSet)
router.register("airplanes", AirplaneViewSet)
router.register("airplane-types", AirplaneTypesViewSet)
router.register("tickets", TicketViewSet)
router.register("orders", OrderViewSet)
urlpatterns = [path("", include(router.urls))]

app_name = "flight"
