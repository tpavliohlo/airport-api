from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    route = models.ForeignKey("Route", on_delete=models.CASCADE, related_name="flights")
    airplane = models.ForeignKey("Airplane", on_delete=models.CASCADE, related_name="airplanes")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ManyToManyField("Crew", related_name="crew")

    def __str__(self):
        return self.route


class Airplane(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey("AirplaneType", on_delete=models.CASCADE, related_name="airplane_types")

    def __str__(self):
        return self.name


class AirplaneType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE, related_name="tickets")
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="orders")


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user.username


class Route(models.Model):
    source = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name="sources")
    destination = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name="destinations")
    distance = models.IntegerField()

    def __str__(self):
        return f"{self.source} -> {self.destination}"


class Airport(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Crew(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
