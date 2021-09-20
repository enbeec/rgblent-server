from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from utils import css_colors
from rgblent_api.models import Color, UserColor
from utils.color import rgb_hex__int_tuple

User = get_user_model()


class Command(BaseCommand):
    help = "Creates CSS Carl!"

    def handle(self, *args, **options):
        carl = User.objects.create_user(
            email="carl@csscarl.com",
            first_name="CSS",
            last_name="Carl",
            last_login=None,
            password="iamcarl",
            username="carl"
        )

        objects = []

        for color in css_colors:
            (r, g, b) = rgb_hex__int_tuple(color["rgb_hex"])
            builtin = True

            color_object = Color(
                red=r, green=g, blue=b, builtin=builtin)

            color_object.save()

            usercolor = UserColor(color_id=color_object.id,
                                  label=color["colorname"], user_id=carl.id)

            objects.append(color_object)
            objects.append(usercolor)

        # if it all ran, we save everything!
        carl.save()
        for new_object in objects:
            new_object.save()
