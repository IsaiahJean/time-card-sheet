from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import TimeCard
from . serializers import TimeCardSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def gaTimeCards(request):
    if request.method == 'GET':
        timeCards = TimeCard.objects.all()
        serializer = TimeCardSerializer(timeCards, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TimeCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def gudTimeCard(request, card_id):
    try:
        timeCard = TimeCard.objects.get(pk=card_id)
    except TimeCard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TimeCardSerializer(timeCard)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TimeCardSerializer(timeCard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        timeCard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
