import self
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.timezone import now
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from flights.models import Flight, Route, Airplane, Crew, Airport, AirplaneType
from flights.serializers import FlightSerializer, FlightListSerializer

FLIGHT_URL = reverse('flight:flight-list')


def detail_url(flight_id):
    return reverse('flight:flight-detail', args=[flight_id,])


def sample_flight(**params) -> Flight:
    # Create source and destination airports
    source_airport = Airport.objects.create(name="Odesa")
    destination_airport = Airport.objects.create(name="Kyiv")

    # Create a route between source and destination airports
    route = Route.objects.create(source=source_airport, destination=destination_airport, distance=500)

    # Create airplane type
    airplane_type = AirplaneType.objects.create(name="Boeing 737 Type")

    # Create an airplane instance with the airplane type
    airplane = Airplane.objects.create(name="Boeing 737", rows=30, seats_in_row=2, airplane_type=airplane_type)

    # Create crew members
    crew_member_1 = Crew.objects.create(first_name="John", last_name="Doe")
    crew_member_2 = Crew.objects.create(first_name="Jane", last_name="Smith")

    # Prepare defaults for flight creation
    defaults = {
        "route": route,
        "airplane": airplane,
        "departure_time": now(),
        "arrival_time": now(),
    }

    # Update defaults with any extra parameters passed to the function
    defaults.update(params)

    # Create the flight instance
    flight = Flight.objects.create(**defaults)

    # Add crew members to the flight (many-to-many relationship)
    flight.crew.set([crew_member_1, crew_member_2])

    return flight


class UnauthenticatedFlightApi(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(FLIGHT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedFlightApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test_username', email='test@test.test', password='testpassword',
        )
        self.client.force_authenticate(self.user)

    def test_flights_list(self):
        sample_flight()

        res = self.client.get(FLIGHT_URL)
        flights = Flight.objects.all()
        serializer = FlightListSerializer(flights, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_flights_detail(self):
        flight = sample_flight()

        url = detail_url(flight.id)

        res = self.client.get(url)

        serializer = FlightListSerializer(flight)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_flight(self):
        payload = {
            "route": "route",
            "airplane": "airplane",
            "departure_time": now(),
            "arrival_time": now(),
        }

        res = self.client.post(FLIGHT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
