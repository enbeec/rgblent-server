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
from rest_framework import status

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
    """(Public) Request handlers for User objects in RGBlent"""

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
    """Request handlers for RGBlent users' own profile"""

    def list(self, request):
        """
            @api {GET} /profile GET the current user's profile
            @apiName GetProfile
            @apiGroup Profile

            @apiUse TokenAuthorization

            @apiSuccess (200) {Object} user Current user's profile 
            @apiSuccess (200) {id} user.id Current user's id
            @apiSuccess (200) {String} user.name Current user's name
            @apiSuccess (200) {String} user.username Current user's username
            @apiSuccess (200) {String} user.email Current user's email
            @apiSuccess (200) {Array} user.colors UserColor objects representing the current user's favorited colors
            @apiSuccess (200) {Array} user.palettes Palette objects representing the current user's saved palettes
            @apiSuccessExample {json} Input
                {
                    "id": 1
                    "name": "Joe Shepherd",
                    "username": "joe",
                    "email": "joe@joeshepherd.com"
                    "colors": []
                    "palettes": []
                }
            """
        user = User.objects.get(pk=request.auth.user.id)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def favorite(self, request):
        """
            @api {POST} /profile/favorite POST new favorite
            @apiName CreateFavorite
            @apiGroup Profile

            @apiUse TokenAuthorization

            @apiSuccess (200) {Object} user_color The newly created UserColor object
            @apiSuccessExample {Object} 
                {
                      "id" => 168,
                   "label" => "my_fave",
                   "color" => {
                            "id" => 174,
                       "rgb_hex" => "#012345",
                           "red" => 1,
                         "green" => 35,
                          "blue" => 69,
                       "builtin" => false,
                    "is_default" => false
                  },
                  "isMine" => true
                }

            @apiError (409 CONFLICT -- Already Exists) {Object} user_color The already created UserColor object
            @apiErrorExample {Object}
                {
                      "id" => 168,
                   "label" => "my_fave",
                   "color" => {
                            "id" => 174,
                       "rgb_hex" => "#012345",
                           "red" => 1,
                         "green" => 35,
                          "blue" => 69,
                       "builtin" => false,
                    "is_default" => false
                  },
                  "isMine" => true
                }
            """
        user = User.objects.get(pk=request.auth.user.id)
        label = request.data['label']
        rgb_hex = request.data['rgb_hex']
        (r, g, b) = rgb_hex__int_tuple(rgb_hex)

        color, _ = Color.objects.get_or_create(red=r, green=g, blue=b)

        user_color, created = UserColor.objects.get_or_create(
            user=user, color=color)

        if created is False:
            serializer = UserColorSerializer(
                user_color, context={'request': request})
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)

        user_color.label = label
        user_color.save()
        serializer = UserColorSerializer(
            user_color, context={'request': request})
        return Response(serializer.data)
