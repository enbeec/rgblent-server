from django.db import models
from django.contrib.auth import get_user
from django.conf import settings

USERCOLOR_LABEL_MAX_LENGTH = 100


class UserColor(models.Model):
    """ UserColor Model
        user (ForeignKey): the user that favorited this color
        color (ForeignKey): the favorited color information
        label (CharField): the favoriting user's name for this color
        """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    color = models.ForeignKey("Color", on_delete=models.RESTRICT)
    label = models.CharField(max_length=USERCOLOR_LABEL_MAX_LENGTH)
