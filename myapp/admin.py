from django.contrib import admin
from .models import Customer, Event

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'date_of_birth')
    search_fields = ('user__username', 'user__email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('customer', 'event_type', 'event_date', 'venue', 'guests')
    search_fields = ('customer__username', 'event_type', 'venue')
    list_filter = ('event_type', 'event_date')
