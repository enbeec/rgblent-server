from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from contextlib import suppress

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'success': True,
            'token': token.key
        }
        return Response(data)
    else:
        data = {'success': False}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    new_user = User.objects.create_user(
        email=request.data['email'],
        password=request.data['password'],
        username=request.data['username'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
    )

    token = Token.objects.create(user=new_user)

    data = {
        'success': True,
        'token': token.key
    }

    return Response(data)
