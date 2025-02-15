from django.db import transaction
from rest_framework import serializers

from flights.models import Flight, Airplane, AirplaneType, Ticket, Order, Route, Airport, Crew


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'


class AirplaneNameSerializer(serializers.ModelSerializer):
    """Only show the name of the Airplane."""
    class Meta:
        model = Airplane
        fields = ["name"]


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True, allow_empty=False)

    class Meta:
        model = Order
        fields = 'id', 'tickets', 'created_at'

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            order = Order.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(order=order, **ticket_data)
            return order


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    source = AirportSerializer(read_only=True)  # Show source airport details
    destination = AirportSerializer(read_only=True)

    class Meta:
        model = Route
        fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="route.source.name", read_only=True)
    destination = serializers.CharField(source="route.destination.name", read_only=True)
    airplane = AirplaneNameSerializer(many=False, read_only=True)

    class Meta:
        model = Flight
        fields = '__all__'


class FlightListSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="route.source.name", read_only=True)
    destination = serializers.CharField(source="route.destination.name", read_only=True)
    airplane = AirplaneNameSerializer(many=False, read_only=True)

    class Meta:
        model = Flight
        fields = ("source", "destination", "airplane", "departure_time", "arrival_time")
