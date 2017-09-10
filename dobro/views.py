from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dobro.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from dobro.models import Profile
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def signup(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        Profile.objects.create(
            email=request.data['email'],
            login=request.data['login'],
            password=make_password(request.data['password']),
        )
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def auth(request):
    try:
        profile = Profile.objects.get(login=request.data['login'])
        if check_password(request.data['password'], profile.password):
            return Response("ok", status=status.HTTP_200_OK)
        else:
            return Response("no", status=status.HTTP_403_FORBIDDEN)
    except Profile.DoesNotExist:
        return Response("No such user", status=status.HTTP_404_NOT_FOUND)