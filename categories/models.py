from django.db import models

from common.models import CommonModel


class Category(CommonModel):
    """Room and Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCE = ("experience", "Experiences")

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=15, choices=CategoryKindChoices.choices)

    def __str__(self) -> str:
        # title() -> 앞의 문자를 대문자로 바꿔줌
        return f'{self.kind.title()}: {self.name}'

    class Meta:
        verbose_name_plural = "Categories"
