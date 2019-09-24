from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import UserDescription
from . serializers import UserDescrSerializer


@api_view(['GET', 'POST'])
def gp_admin_users(request):
    if request.method == 'GET':
        user_description = UserDescription.objects.all()
        serializer = UserDescrSerializer(user_description, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserDescrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
