from django.db import models
from django.contrib.auth import get_user

User = get_user_model()
USERCOLOR_LABEL_MAX_LENGTH = 100


class UserColor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.ForeignKey("Color", on_delete=models.RESTRICT)
    label = models.CharField(max_length=USERCOLOR_LABEL_MAX_LENGTH)
