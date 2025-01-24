from folder_aplikacji.models import Dog, Cat
from folder_aplikacji.serializers import DogSerializer, CatSerialier
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# TESTOWANIE
# tworzymy nowe obiekty 

dog = Dog.objects.create(name = 'pimpek', age)

# reszte w shellu pisalem 
# caly pies dziala jak pies dziala to reszta dziala