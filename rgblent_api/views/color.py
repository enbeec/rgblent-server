from django.conf import settings
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import AllowAny
from rgblent_api.models import Color, UserColor
from utils.color import color_info


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        # TODO: handle alpha
        fields = ('id', 'rgb_hex', 'red', 'green',
                  'blue', 'builtin', 'is_default')


class UserColorSerializer(serializers.ModelSerializer):
    color = ColorSerializer()

    class Meta:
        model = UserColor
        fields = ('label', 'color')


class ColorView(ViewSet):
    def list(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(
            colors, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        colors = Color.objects.get(pk=pk)
        serializer = ColorSerializer(
            colors, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def defaults(self, request):
        colors = Color.objects.filter(is_default=True)
        serializer = ColorSerializer(
            colors, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def favorite(self, request, pk=None):
        color = Color.objects.filter(pk=pk)
        user_color = UserColor(color=color, label=request.data['label'])
        serializer = UserColorSerializer(
            user_color, context={'request': request})
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def colorinfo(request):
    rgb_hex = request.data["rgb_hex"]
    return Response(color_info(rgb_hex))


@api_view(['GET'])
@permission_classes([AllowAny])
def default_colors(request):
    colors = Color.objects.filter(is_default=True)
    serializer = ColorSerializer(
        colors, many=True, context={'request': request})
    return Response(serializer.data)
