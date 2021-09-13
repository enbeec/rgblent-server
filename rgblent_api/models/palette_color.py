from django.db import models
from django.conf import settings

PALETTECOLOR_LABEL_MAX_LENGTH = 100


class PaletteColor(models.Model):
    palette = models.ForeignKey("Palette", on_delete=models.CASCADE)
    # RESTRICT keeps colors from being deleted if they are referenced somewhere
    color = models.ForeignKey("Color", on_delete=models.RESTRICT)
    label = models.CharField(max_length=PALETTECOLOR_LABEL_MAX_LENGTH)
