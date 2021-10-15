from django.conf import settings
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import AllowAny
from rgblent_api.models import Palette, PaletteColor
from .color import ColorSerializer


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
        fields = ('name', 'colors')

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
