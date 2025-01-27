from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.decorators import parser_classes
from django.http import HttpResponse
import datetime
from .models import Dog, Cat, Osoba, Money_collection, Shelter, Cage
from .serializers import DogSerializer, CatSerializer, OsobaSerializer, Money_collectionSerializer, ShelterSerializer, CageSerializer
from .authentication import BearerTokenAuthentication, check_permission
from django.core.exceptions import PermissionDenied


#DLA PSA
# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET', 'POST'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def dog_list(request):
    """
    Lista wszystkich obiektów modelu Person.
    """
    if request.method == 'GET':
        check_permission(request.user, 'folder_aplikacji.view_dog') # tu masz do get
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        check_permission(request.user, 'folder_aplikacji.add_dog') # tu masz do post 
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
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
        check_permission(request.user, 'folder_aplikacji.view_dog') #tu masz do get
        dog = Dog.objects.get(pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        check_permission(request.user, 'folder_aplikacji.change_dog') # tu masz do put
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        check_permission(request.user, 'folder_aplikacji.delete_dog') # tu masz delate
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# DLA KOTA
@api_view(['GET', 'POST'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def cat_list(request):

     if request.method == 'GET':
        check_permission(request.user, 'folder_aplikacji.view_cat') # tu masz do get
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)
    
     elif request.method == 'POST':
        check_permission(request.user, 'folder_aplikacji.add_cat') # tu masz do post 
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def cat_detail(request, pk):

    try:
        cat = Cat.objects.get(pk=pk)
    except Cat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        check_permission(request.user, 'folder_aplikacji.view_cat')
        cat = Cat.objects.get(pk=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        check_permission(request.user, 'folder_aplikacji.change_cat')
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        check_permission(request.user, 'folder_aplikacji.delate.cat')
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#USER
@api_view(['GET', 'POST'])
#@authentication_classes([BearerTokenAuthentication])
#@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def osoba_list(request):

    if request.method == 'GET' :
        check_permission(request.user, 'auth.view_user')
        osoby = Osoba.objects.filter(boss=request.user)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        check_permission(request.user, 'auth.add_user')
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(boss = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
#@authentication_classes([BearerTokenAuthentication])
#@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def osoba_detail(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        check_permission(request.user, 'auth.view_user')
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        check_permission(request.user, 'auth.delete_user')
        osoba.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
# ZBIORKA
@api_view (['GET', 'POST'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def money_collection_list(request):
    check_permission(request.user, 'folder_aplikacji.view_money_collection')
    if request.method == 'GET':
        moneys_collection = Money_collection.objects.all()
        serializer = Money_collectionSerializer(moneys_collection, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        check_permission(request.user, 'folder_aplikacji.add_money_collection')
        serializer = Money_collectionSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view (['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def money_collection_detail(request, pk):
    try:
        money_collection = Money_collection.objects.get(pk=pk)
    except Money_collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        check_permission(request.user, 'folder_aplikacji.view_money_collection')
        money_collection = Money_collection.objects.get(pk=pk)
        serializer = Money_collectionSerializer(money_collection)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        check_permission(request.user, 'folder_aplikacji.change_money_collection')
        serializer = Money_collectionSerializer(money_collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        check_permission(request.user, 'folder_aplikacji.delete_money_collection')
        money_collection.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#SCHRONISKO
@api_view (['GET', 'POST'])
@parser_classes([JSONParser])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def shelter_list(request):
    if request.method == 'GET':
        check_permission(request.user, 'folder_aplikacji.view_shelter')
        shelters = Shelter.objects.all()
        serializer = ShelterSerializer(shelters, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        check_permission(request.user, 'folder_aplikacji.add_shelter')
        serializer = ShelterSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def shelter_detail(request, pk):
    try:
        shelter = Shelter.objects.get(pk=pk)
    except Shelter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        check_permission(request.user, 'folder_aplikacji.view_shelter')
        shelter = Shelter.objects.get(pk=pk)
        serializer = ShelterSerializer(shelter)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        check_permission(request.user, 'folder_aplikacji.change_shelter')
        serializer = ShelterSerializer(shelter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        check_permission(request.user, 'folder_aplikacji.delete_shelter')
        shelter.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#KLATKA
@api_view(['GET', 'POST'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def cage_list(request):

    if request.method == 'GET' :
        check_permission(request.user, 'folder_aplikacji.view_cage')
        cages = Cage.objects.all()
        serializer = CageSerializer(cages, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        check_permission(request.user, 'folder_aplikacji.add_cage')
        serializer = CageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT', 'DELETE'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def cage_detail(request, pk):
    try:
        cage = Cage.objects.get(pk=pk)
    except Cage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        check_permission(request.user, 'folder_aplikacji.view_cage')
        cage = Cage.objects.get(pk=pk)
        serializer = CageSerializer(cage)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        check_permission(request.user, 'folder_aplikacji.change_cage')
        serializer = CageSerializer(cage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        check_permission(request.user, 'folder_aplikacji.delete_cage')
        cage.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
#HTML # ZROBILEM TYLKO DLA PSA ZA MALO CZASU
def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witamy w Schronisku </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def dog_list_html(request):
    dogs = Dog.objects.all()
    return render(request, 'folder_aplikacji/dog/list.html', {'dogs': dogs})

def dog_detail_html(request, pk):
    dog = Dog.objects.get(id=pk)
    return render(request,
                  "folder_aplikacji/dog/detail.html",
                  {'dog': dog})
    




    


    
