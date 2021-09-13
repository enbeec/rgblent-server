from django.db import models
from django.core.validators import MaxValueValidator


class Color(models.Model):
    red = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(255)])
    green = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(255)])
    blue = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(255)])
    alpha = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(255)])
    is_default = models.BooleanField(default=False)
