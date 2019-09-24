from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import UserDescription
from . serializers import UserDescrSerializer, UserSerializer, AddDescriptionSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def g_users(request):
    user_description = UserDescription.objects.all()
    serializer = UserDescrSerializer(user_description, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def p_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def g_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def p_description(request):
    serializer = AddDescriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

