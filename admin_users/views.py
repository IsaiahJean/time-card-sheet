from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import UserDescription
from . serializers import UserDescrSerializer, UserSerializer, AddDescriptionSerializer, ESerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# All users with description
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def g_users(request):
    user_description = UserDescription.objects.all()
    serializer = UserDescrSerializer(user_description, many=True)
    return Response(serializer.data)

# Add user without description
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def p_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get user without description by username, where username = email(!!!)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def g_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

# Add description to existing user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def p_description(request):
    serializer = AddDescriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Edit and Get description
@api_view(['PATCH', 'GET'])
@permission_classes([IsAuthenticated])
def edit_description(request, id_user):
    try:
        user = UserDescription.objects.get(id=id_user)
    except UserDescription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        serializer = ESerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = ESerializer(user)
        return Response(serializer.data)

# Edit, get, and delete user
@api_view(['PATCH', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def edit_user(request, id_user):
    try:
        userD = UserDescription.objects.get(id=id_user)
        user = User.objects.get(id=userD.user.id)
    except UserDescription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
