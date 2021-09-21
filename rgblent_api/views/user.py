from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rgblent_api.models import UserColor
from .palette import PaletteSerializer
from .color import ColorSerializer

User = get_user_model()


class UserColorSerializer(serializers.ModelSerializer):
    color = ColorSerializer()

    class Meta:
        model = UserColor
        fields = ('label', 'color')


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    colors = UserColorSerializer(many=True)
    palettes = PaletteSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'colors', 'palettes')

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


@permission_classes([AllowAny])
class UserView(ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
