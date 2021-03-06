from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from contextlib import suppress

User = get_user_model()

""" @apiDefine TokenAuthorization
    @apiHeader {String} Authorization Auth token
    @apiHeaderExample {String} Authorization 
        Token 9ba45f09651c5b0c404f37a2d2572c026c146694
    """


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
            @api {POST} /login Login and recieve token
            @apiName Login
            @apiGroup Authentication

            @apiParam {String} username Username            
            @apiParam {String} password Password            
            @apiParamExample {json}
                {
                    "username": "joe",
                    "password": "shep",
                }

            @apiSuccess (200) {Object} credentials Logged in user's credentials
            @apiSuccess (200) {credentials.token} Logged in user's authorization token
            @apiSuccessExample (200) {json}
                {
                    "token": "9ba45f09651c5b0c404f37a2d2572c026c146694"
                }
            """
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
    """
            @api {POST} /register Register and recieve token
            @apiName Register 
            @apiGroup Authentication

            @apiParam {String} username Username            
            @apiParam {String} password Password            
            @apiParam {String} first_name First name
            @apiParam {String} last_name Last name
            @apiParam {String} email Email
            @apiParamExample {json}
                {
                    "first_name": "Joe",
                    "last_name": "Shepherd",
                    "email": "joe@joeshepherd.com",
                    "username": "joe",
                    "password": "shep",
                }

            @apiSuccess (200) {Object} credentials Registered user's credentials
            @apiSuccess (200) {credentials.} credentials.token Registered user's authorization token
            @apiSuccessExample (200) {json}
                {
                    "token": "9ba45f09651c5b0c404f37a2d2572c026c146694"
                }
            """
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
