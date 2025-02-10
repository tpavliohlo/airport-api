from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from flights.models import Flight, Airplane, AirplaneType, Ticket, Order, Route, Airport, Crew
from flights.serializers import FlightSerializer, AirplaneSerializer, AirplaneTypeSerializer, TicketSerializer, \
    OrderSerializer, RouteSerializer, AirportSerializer, CrewSerializer, FlightListSerializer


class FlightViewSet(
    viewsets.ModelViewSet
):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class AirplaneViewSet(
viewsets.ModelViewSet
):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneTypesViewSet(
viewsets.ModelViewSet
):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class TicketViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class RouteViewSet(
viewsets.ModelViewSet
):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class AirportViewSet(
    viewsets.ModelViewSet
):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class CrewViewSet(
    viewsets.ModelViewSet
):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
