from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices, )

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "pets_friendly",
        "kind",
        "amenities",
    )

    # contains (포함되어 있는지) 로 찾음
    search_fields = (
        # ^ -> startswith
        "name",
        "^price",
        # "=price", equals
        "owner__username",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
