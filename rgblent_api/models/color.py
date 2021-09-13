from django.db import models
from django.core.validators import MaxValueValidator


class Color(models.Model):
    """Color Model

        Fields:
            red (PositiveSmallIntegerField): red value
            green (PositiveSmallIntegerField): green value
            blue (PositiveSmallIntegerField): blue value
            alpha (PositiveSmallIntegerField): alpha value
            is_default (BooleanField): indicates if the color is one of the defaults
        """
    red = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(255)])
    green = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(255)])
    blue = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(255)])
    alpha = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(255)])
    is_default = models.BooleanField(default=False)
