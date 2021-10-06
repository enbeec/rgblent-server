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
            {
                TODO
            }
        """
    palette = Palette.objects.get(builtin=True, name="default")
    serializer = PaletteSerializer(palette, context={'request': request})
    return Response(serializer.data)
