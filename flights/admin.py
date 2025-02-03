from django.contrib import admin

from flights.models import Flight, Crew, Route, Airport, Order, Ticket, AirplaneType, Airplane

admin.site.register(Flight)
admin.site.register(Airplane)
admin.site.register(AirplaneType)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(Route)
admin.site.register(Airport)
admin.site.register(Crew)
