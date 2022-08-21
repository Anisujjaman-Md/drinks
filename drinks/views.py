from os import RWF_APPEND
from unittest import expectedFailure
from urllib import request
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    #get all from drinnks , serialize them and return json
    if request.method == 'GET': 
        drinks = Drink.objects.all()
        serializer = DrinksSerializer(drinks, many =True)

        return JsonResponse({'drinks' : serializer.data} )

    if request.method == 'POST':
        serializer =DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = DrinksSerializer(drink)
        return Response(serializer.data)


    if request.method == 'PUT':
        pass

    if request.method == 'DELETE':
        pass
