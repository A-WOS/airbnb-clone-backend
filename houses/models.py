from django.db import models


class House(models.Model):
    """Model Definition for Houses"""

    name = models.CharField(
        max_length=140,
        verbose_name="이름",
    )
    price_per_night = models.PositiveIntegerField(
        verbose_name="가격",
        help_text="양수만 됩니다.",
    )
    description = models.TextField()
    address = models.CharField(
        max_length=140,
        verbose_name="주소",
        help_text="주소 기입"
    )
    pets_allowed = models.BooleanField(
        verbose_name="애완 동물 가능?",
        default=True,
        help_text="애완 동물 반입 여부",
    )

    def __str__(self):
        return self.name
