from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.decorators import parser_classes
from .models import Dog, Cat, Osoba, Money_collection, Shelter, Cage
from .serializers import DogSerializer, CatSerializer, OsobaSerializer, Money_collectionSerializer, ShelterSerializer, CageSerializer


#DLA PSA
# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET'])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def dog_list(request):
    """
    Lista wszystkich obiektów modelu Person.
    """
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser, FormParser, MultiPartParser])
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
@parser_classes([JSONParser, FormParser, MultiPartParser])
def cat_list(request):

    if request.method == 'GET' :
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser, FormParser, MultiPartParser])
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
    
    elif request.method == 'DELETE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#USER
@api_view(['GET', 'POST'])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def osoba_list(request):

    if request.method == 'GET' :
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def osoba_detail(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
# ZBIORKA
@api_view (['GET', 'POST'])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def money_collection_list(request):
    if request.method == 'GET':
        moneys_collection = Money_collection.objects.all()
        serializer = Money_collectionSerializer(moneys_collection, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = Money_collectionSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view (['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def money_collection_detail(request, pk):
    try:
        money_collection = Money_collection.objects.get(pk=pk)
    except Money_collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        money_collection = Money_collection.objects.get(pk=pk)
        serializer = Money_collectionSerializer(money_collection)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = Money_collectionSerializer(money_collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        money_collection.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#SCHRONISKO
@api_view (['GET', 'POST'])
@parser_classes([JSONParser])
def shelter_list(request):
    if request.method == 'GET':
        shelters = Shelter.objects.all()
        serializer = ShelterSerializer(shelters, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ShelterSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser])
def shelter_detail(request, pk):
    try:
        shelter = Shelter.objects.get(pk=pk)
    except Shelter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        shelter = Shelter.objects.get(pk=pk)
        serializer = ShelterSerializer(shelter)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ShelterSerializer(shelter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        shelter.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#KLATKA
@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def cage_list(request):

    if request.method == 'GET' :
        cages = Cage.objects.all()
        serializer = CageSerializer(cages, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser])
def cage_detail(request, pk):
    try:
        cage = Cage.objects.get(pk=pk)
    except Cage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        cage = Cage.objects.get(pk=pk)
        serializer = CageSerializer(cage)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CageSerializer(cage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        cage.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



    


    
