from django.db import models
from django.conf import settings

PALETTECOLOR_LABEL_MAX_LENGTH = 100


class PaletteColor(models.Model):
    """ Palette Color Model

        Fields:
            palette (ForeignKey): the palette this color belongs to
            color (ForeignKey): the color to associate with the palette
            label (CharField): the label for this color in the context of this palette
        """
    palette = models.ForeignKey(
        "Palette", related_name="colors", on_delete=models.CASCADE)
    # RESTRICT keeps colors from being deleted if they are referenced somewhere
    color = models.ForeignKey(
        "Color", related_name="palette_color", on_delete=models.RESTRICT)
    label = models.CharField(max_length=PALETTECOLOR_LABEL_MAX_LENGTH)
    builtin = models.BooleanField(default=False)
