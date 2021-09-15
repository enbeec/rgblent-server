from django.conf import settings
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action
from rgblent_api.models import Color, UserColor


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        # TODO: handle alpha
        fields = ('id', 'rgb_hex', 'red', 'green',
                  'blue', 'builtin', 'is_default')


class ColorView(ViewSet):
    def list(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(
            colors, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # TODO: search favorites by label
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
