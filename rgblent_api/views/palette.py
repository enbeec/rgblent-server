from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import AllowAny
from rgblent_api.models import Palette, PaletteColor, Color
from .color import ColorSerializer
from utils.color import rgb_hex__int_tuple

User = get_user_model()


class PaletteColorSerializer(serializers.ModelSerializer):
    """ JSON serializer for PaletteColor

        Arguments:
            serializers
        """
    color = ColorSerializer()

    class Meta:
        model = PaletteColor
        fields = ('builtin', 'label', 'color')


class PaletteSerializer(serializers.ModelSerializer):
    """ JSON serializer for Palette

        Arguments:
            serializers
        """
    colors = PaletteColorSerializer(many=True)
    isMine = serializers.SerializerMethodField()

    class Meta:
        model = Palette
        fields = ('id', 'name', 'colors', 'isMine')

    def get_isMine(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        if user is not None and obj.user is not None:
            return user.id == obj.user.id

        return False


class PaletteView(ViewSet):
    def list(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        name = request.query_params.get('name', None)
        if name is not None:
            palette = Palette.objects.get(name=name)
            serializer = PaletteSerializer(
                palette, context={'request': request})
        else:
            palettes = Palette.objects.all()
            serializer = PaletteSerializer(
                palettes, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        name = request.data["name"]

        try:
            palette = Palette.objects.get(name=name)
        except Palette.DoesNotExist as ex:
            palette = Palette(user=user, name=name)
            palette.save()

        colors = request.data["colors"]

        color_objs = []
        palette_color_objs = []

        for color in colors:
            (r, g, b) = rgb_hex__int_tuple(color["rgb_hex"])

            try:
                color_obj = Color.objects.get(red=r, green=g, blue=b)
            except Color.DoesNotExist as ex:
                color_obj = Color(red=r, green=g, blue=b)

            palette_color = PaletteColor(
                palette=palette, color=color_obj, label=color["label"])

            color_objs.append(color_obj)
            palette_color_objs.append(palette_color)

        for obj in color_objs:
            obj.save()

        for obj in palette_color_objs:
            obj.save()

        serializer = PaletteSerializer(palette, context={'request': request})
        return Response(serializer.data)

    def get_isMine(self, obj):
        """ Returns true if request user matches the palette being serialized

            Arguments:
                self -- the serializer instance
                obj -- the Palette being serialized
            """
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        if user is not None:
            return user.id == obj.user.id

        return False


@api_view(['GET'])
@permission_classes([AllowAny])
def default_palette(request):
    """
        @api {GET} /default/palette GET default palette
        @apiName DefaultPalette
        @apiGroup Palette

        @apiSuccess (200) {Object} palette Retrieved default palette
        @apiSuccessExample {json} Success
            [
                  {
                       "rgb_hex" => "#FFDF80",
                           "red" => 255,
                         "green" => 223,
                          "blue" => 128,
                       "builtin" => false,
                    "is_default" => true
                  },
                  {
                       "rgb_hex" => "#BFFF80",
                           "red" => 191,
                         "green" => 255,
                          "blue" => 128,
                       "builtin" => false,
                    "is_default" => true
                  },
                  {
                       "rgb_hex" => "#80FF9F",
                           "red" => 128,
                         "green" => 255,
                          "blue" => 159,
                       "builtin" => false,
                    "is_default" => true
                  },
                  {
                       "rgb_hex" => "#80FFFF",
                           "red" => 128,
                         "green" => 255,
                          "blue" => 255,
                       "builtin" => false,
                    "is_default" => true
                  },
                  {
                       "rgb_hex" => "#809FFF",
                           "red" => 128,
                         "green" => 159,
                          "blue" => 255,
                       "builtin" => false,
                    "is_default" => true
                  },
                  {
                       "rgb_hex" => "#BF80FF",
                           "red" => 191,
                         "green" => 128,
                          "blue" => 255,
                       "builtin" => false,
                    "is_default" => true
                  },
                  {
                       "rgb_hex" => "#FF80DF",
                           "red" => 255,
                         "green" => 128,
                          "blue" => 223,
                       "builtin" => false,
                    "is_default" => true
                  },
                  {
                       "rgb_hex" => "#FF8080",
                           "red" => 255,
                         "green" => 128,
                          "blue" => 128,
                       "builtin" => false,
                    "is_default" => true
                  }
            ]
        """
    palette = Palette.objects.get(builtin=True, name="default")
    serializer = PaletteSerializer(palette, context={'request': request})
    return Response(serializer.data)
