from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from .models import Dog, Cat, User, Money_collection, Shelter, Cage
from .serializers import DogSerializer, CatSerializer, UserSerializer, Money_collectionSerializer, Shelter, Cage


#DLA PSA
# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def dog_list(request):
    """
    Lista wszystkich obiektów modelu Person.
    """
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def dog_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Person
    :return: Response (with status and/or object/s data)
    """
    try:
        dog = Dog.objects.get(pk=pk)
    except Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Person.
    """
    if request.method == 'GET':
        dog = Dog.objects.get(pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# DLA KOTA
@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def cat_list(request):

    if request.method == 'GET' :
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELATE'])
@parser_classes([MultiPartParser, FormParser])
def cat_detail(request, pk):

    try:
        cat = Cat.objects.get(pk=pk)
    except Cat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        cat = Cat.objects.get(pk=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELATE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#USER
@api_view(['GET'])
def user_list(request):

    if request.method == 'GET' :
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
