from track.models import DietActivity, Event, HobbyActivity, Measurement, MyStats, PhysicalActivity, TargetMeasurement
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    list_display = ['type', 'start', 'end']
    search_fields = ['type']

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['type', 'value', 'unit', 'timestamp']
    search_fields = ['type']

class PhysicalActivityAdmin(admin.ModelAdmin):
    list_display = ['event', 'distance', 'reps', 'caloriesBurnt']
    search_fields = ['event']

class DietActivityAdmin(admin.ModelAdmin):
    list_display = ['event', 'mealType']
    search_fields = ['event']

class TargetMeasurementAdmin(admin.ModelAdmin):
    list_display = ['type', 'value', 'unit']

admin.site.register(DietActivity, DietActivityAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(HobbyActivity)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(MyStats)
admin.site.register(PhysicalActivity, PhysicalActivityAdmin)
admin.site.register(TargetMeasurement, TargetMeasurementAdmin)

