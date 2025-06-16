from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

# Register CarMake with inline CarModel editing
admin.site.register(CarMake, CarMakeAdmin)

# Register CarModel separately (if needed)
admin.site.register(CarModel)
