from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class DDD:
    CHOICES = (
        ("011", "011"),
        ("016", "016"),
        ("017", "017"),
        ("018", "018"),
    )


class Plan:
    DEFAULT = ""
    TALK_MORE_LOW = "talk_more_low"
    TALK_MORE_MEDIUM = "talk_more_medium"
    TALK_MORE_HIGH = "talk_more_high"

    CHOICES = (
        (DEFAULT, ""),
        (TALK_MORE_LOW, "FaleMais30"),
        (TALK_MORE_MEDIUM, "FaleMais60"),
        (TALK_MORE_HIGH, "FaleMais120"),
    )


class Call(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="created by", null=True
    )
    origin = models.CharField(choices=DDD.CHOICES, max_length=3)
    destiny = models.CharField(choices=DDD.CHOICES, max_length=3)
    talk_more_tariff = models.FloatField()
    default_tariff = models.FloatField()
    plan = models.CharField(
        choices=Plan.CHOICES, default=Plan.DEFAULT, max_length=20, blank=True
    )
    minutes = models.PositiveIntegerField()
