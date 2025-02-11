from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from flights.models import Flight, Airplane, AirplaneType, Ticket, Order, Route, Airport, Crew
from flights.permissions import IsAdminOrIfAuthenticatedReadOnly
from flights.serializers import FlightSerializer, AirplaneSerializer, AirplaneTypeSerializer, TicketSerializer, \
    OrderSerializer, RouteSerializer, AirportSerializer, CrewSerializer, FlightListSerializer


class FlightViewSet(
    viewsets.ModelViewSet
):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class AirplaneViewSet(
viewsets.ModelViewSet
):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class AirplaneTypesViewSet(
viewsets.ModelViewSet
):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


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
    permission_classes = (IsAuthenticated,)


class RouteViewSet(
viewsets.ModelViewSet
):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class AirportViewSet(
    viewsets.ModelViewSet
):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class CrewViewSet(
    viewsets.ModelViewSet
):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
