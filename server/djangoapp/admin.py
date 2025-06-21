from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.StackedInline):

    model = CarModel
    extra = 2


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):

    inlines = [CarModelInline]
    list_display = ['name', 'description']


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):

    list_display = ['car_make', 'name', 'type', 'year', 'color']
    list_filter = ['car_make']
    search_fields = ['car_make', 'name', 'type']


# Register CarMake with inline CarModel editing
admin.site.register(CarMake, CarMakeAdmin)

# Register CarModel separately (if needed)
admin.site.register(CarModel, CarModelAdmin)

