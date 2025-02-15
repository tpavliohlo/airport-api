from django.contrib import admin

from flights.models import Flight, Crew, Route, Airport, Order, Ticket, AirplaneType, Airplane


class TicketInLine(admin.TabularInline):
    model = Ticket
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [TicketInLine,]


admin.site.register(Flight)
admin.site.register(Airplane)
admin.site.register(AirplaneType)
admin.site.register(Ticket)
admin.site.register(Route)
admin.site.register(Airport)
admin.site.register(Crew)
