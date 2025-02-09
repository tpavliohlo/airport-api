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
    class Meta:
        model = Order
        fields = '__all__'


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
    #route = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all())
    route = RouteSerializer(many=False, read_only=True)
    airplane = AirplaneNameSerializer(many=False, read_only=True)

    class Meta:
        model = Flight
        fields = '__all__'

