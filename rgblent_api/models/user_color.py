from django.db import models
from django.conf import settings

USERCOLOR_LABEL_MAX_LENGTH = 100


class UserColor(models.Model):
    """ UserColor Model

        Fields:
            user (ForeignKey): the user that favorited this color
            color (ForeignKey): the favorited color information
            label (CharField): the favoriting user's name for this color
        """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    # RESTRICT keeps colors from being deleted if they are referenced somewhere
    color = models.ForeignKey("Color", on_delete=models.RESTRICT)
    label = models.CharField(max_length=USERCOLOR_LABEL_MAX_LENGTH)
