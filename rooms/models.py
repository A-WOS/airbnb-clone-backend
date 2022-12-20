from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    """Room model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pets_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms",)
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms",)
    category = models.ForeignKey("categories.Category", null=True, default="", on_delete=models.SET_NULL, related_name="rooms",)

    def __str__(self) -> str:
        return self.name

    def total_amenities(self) -> int:
        return self.amenities.count()


class Amenity(CommonModel):
    """Amenity model Definition"""

    name = models.CharField(max_length=150)
    # default="" 대신에 null=True 로 작성 가능
    # blank=True 는 Django form 에서 공백을 의미
    # default="" 는 db 에서 null 을 의미
    description = models.CharField(max_length=150, blank=True, default="")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
