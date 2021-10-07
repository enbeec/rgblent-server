from django.conf import settings
from rest_framework import status
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import AllowAny
from rgblent_api.models import Color, UserColor
from utils import color_info, colorblend


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        # TODO: handle alpha
        fields = ('id', 'rgb_hex', 'red', 'green',
                  'blue', 'builtin', 'is_default')


class UserColorSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    isMine = serializers.SerializerMethodField()

    class Meta:
        model = UserColor
        fields = ('id', 'label', 'color', 'isMine')

    def get_isMine(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        if user is not None and obj.user is not None:
            return user.id == obj.user.id

        return False


class ColorView(ReadOnlyModelViewSet):
    """ TODO: apidoc entries for list and retrieve """
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


@api_view(['POST'])
@permission_classes([AllowAny])
def colorinfo(request):
    """ @api {POST} /colorinfo POST get detailed information on a color
        @apiName Info
        @apiGroup Color

        @apiParam {String} rgb_hex The provided color as a hex string
        @apiParamExample {json}
            {
                "rgb_hex": "#405060"
            }

        @apiSuccess (200) {Object} color_info The provided color translated to different colorspaces
        @apiSuccessExample (200) {json}
            {
                "rgb": {
                    "rgb_r": 64.0,
                    "rgb_g": 80.0,
                    "rgb_b": 96.0,
                    "is_upscaled": false,
                },
                "hsl": {
                    "hsl_h": 210.0,
                    "hsl_s": -0.202531645556962025,
                    "hsl_l": 80.0
                },
                "hsv": {
                    "hsv_h": 210.0,
                    "hsv_s": 0.3333333333337,
                    "hsv_v": 96.0
                },
                "lab": {
                    "lab_l": 3636.209104440874,
                    "lab_a": -150.7336722215644,
                    "lab_b": -982.4912665013201,
                    "observer": "2",
                    "illuminant": "d65",
                },
                "xyz": {
                    "xyz_x": 28581.772648563052,
                    "xyz_y": 30954.276615825478,
                    "xyz_z": 52127.62204019337,
                    "observer": "2",
                    "illuminant": "d65",
                }
            }
        """
    rgb_hex = request.data["rgb_hex"]
    return Response(color_info(rgb_hex))


@api_view(['POST'])
@permission_classes([AllowAny])
def colorblend(request):
    """
        @api {POST} /colorblend POST two colors and get the result of blending them together
        @apiName Blend
        @apiGroup Color
        """
    rgb_hex1 = request.data["color_a"]
    rgb_hex2 = request.data["color_b"]
    rgb_hex_new = color_blend(rgb_hex1, rgb_hex2)
    return Response({"rgb_hex": rgb_hex_new[:7]})


@api_view(['GET'])
@permission_classes([AllowAny])
def default_colors(request):
    colors = Color.objects.filter(is_default=True)
    serializer = ColorSerializer(
        colors, many=True, context={'request': request})
    return Response(serializer.data)
