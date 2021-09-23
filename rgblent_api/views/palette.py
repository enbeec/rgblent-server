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
    color = ColorSerializer()

    class Meta:
        model = PaletteColor
        fields = ('builtin', 'label', 'color')


class PaletteSerializer(serializers.ModelSerializer):
    colors = PaletteColorSerializer(many=True)

    class Meta:
        model = Palette
        fields = ('id', 'name', 'colors')


class PaletteView(ViewSet):
    def create(self, request):
        name = request.data["name"]
        # ignore all but the first 8 colors just in case
        colors = request.data["colors"][0:7]

        # create a palette

        color_objs = []
        palette_color_objs = []

        # for each color:
        #   make sure it exists
        #   add to the array
        #   make a palette_color
        #   add to the array

        # save everything
        # return the serialized palette


@api_view(['GET'])
@permission_classes([AllowAny])
def default_palette(request):
    palette = Palette.objects.get(builtin=True, name="default")
    serializer = PaletteSerializer(palette, context={'request': request})
    return Response(serializer.data)
