from django.db import models
from django.conf import settings

PALETTE_NAME_MAX_LENGTH = 100


class Palette(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=PALETTE_NAME_MAX_LENGTH)
