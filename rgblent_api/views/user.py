from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import AllowAny
from rgblent_api.models import Color, UserColor
from .palette import PaletteSerializer
from .color import ColorSerializer, UserColorSerializer
from utils.color import rgb_hex__int_tuple

User = get_user_model()


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


class ProfileView(ViewSet):
    def list(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def favorite(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        label = request.data['label']
        rgb_hex = request.data['rgb_hex']
        print(f"{rgb_hex} {label}")
        (r, g, b) = rgb_hex__int_tuple(rgb_hex)

        try:
            color = Color.objects.get(red=r, green=g, blue=b)
        except Color.DoesNotExist as ex:
            color = Color(red=r, green=g, blue=b)
            color.save()

        try:
            user_color = UserColor.objects.get(color=color)
            # FIXME: add a proper return code
            return Response("color already exists")
        except UserColor.DoesNotExist as ex:
            print(f"{rgb_hex} {label}")
            user_color = UserColor(user=user, color=color, label=label)
            user_color.save()

            serializer = UserColorSerializer(
                user_color, context={'request': request})
            return Response(serializer.data)
