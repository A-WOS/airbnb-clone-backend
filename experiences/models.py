from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """Experience model Definition"""
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    # TimeField 는 시 분 초만 저장
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField(blank=True, null=True)
    perks = models.ManyToManyField("experiences.Perk")

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):
    """What is included on an Experience"""

    name = models.CharField(max_length=100)
    details = models.CharField(max_length=250, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
