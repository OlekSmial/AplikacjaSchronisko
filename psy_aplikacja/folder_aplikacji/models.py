from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

AGE_CHOICES =[
    ('kitten', 'Kociak'),
    ('puppy', 'Szczeniak'),
    ('age', 'Wiek')
]

CASTRATED_CHOICES =[
    ('YES','TAK'),
    ('NO','NIE')
]


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Dog(models.Model):

    name = models.CharField(max_length=60) #imie psa
    rasa_psa = models.CharField(max_length=60) # rasa psa
    SIZE = models.CharField(max_length=1, choices=SIZE, default=SIZE[0][0]) #wielkosc psa
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0]) #miesiac dodania ogloszenia
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL) #gotowy do adopcji lub nie 
    age_type = models.CharField(max_length=10, choices=AGE_CHOICES, default='age') #wiek typ
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(99)]) # wiek
    castrated = models.CharField(max_length=10, choices=CASTRATED_CHOICES, default="") #czy pies jest wykastrowany

class Cat(models.Model):

    name = models.CharField(max_length=60) #imie kota
    rasa_kota = models.CharField(max_length=60) # rasa kota
    SIZE = models.CharField(max_length=1, choices=SIZE, default=SIZE[0][0]) #wielkosc kota
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0]) #miesiac dodania ogloszenia
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL) #gotowy do adopcji lub nie 
    age_type = models.CharField(max_length=10, choices=AGE_CHOICES, default='age') #wiek typ
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(99)]) # wiek
    castrated = models.CharField(max_length=10, choices=CASTRATED_CHOICES, default="") #czy kot jest wykastrowany




    def __str__(self):
        if self.age_type == 'puppy' :
            return "Szczeniak"
        if self.age_type == 'kitten' :
            return "Kociak"
        return f"Wiek: {self.age} lat"

    def __str__(self):
        return self.name