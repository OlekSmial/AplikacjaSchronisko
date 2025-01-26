from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.core.validators import EmailValidator

# Create your models here.
# duzo modeli wzietych z dokumentacji bodajze lab 04
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
    ('age', 'Wiek'),
    ('adult', 'dorosly')
]

CASTRATED_CHOICES =[
    ('YES','TAK'),
    ('NO','NIE'),
    ("",'Nie podano'),
]

STATUS_CHOICES = [
    ('free', 'Wolna'),
    ('occupied', 'Zajęta')
]

class Dog(models.Model):

    image = models.ImageField(upload_to='images/', blank=True, null=True) #zdjecir zwierzaka
    name = models.CharField(max_length=60) #imie psa
    rasa_psa = models.CharField(max_length=60, blank=True) # rasa psa
    SIZE = models.CharField(max_length=1,choices=SIZE, default=SIZE[0][0]) #wielkosc psa
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0]) #miesiac dodania ogloszenia
    team = models.CharField(max_length=60, default="") #gotowy do adopcji lub nie 
    age_type = models.CharField(max_length=10, choices=AGE_CHOICES, default='age') #wiek typ
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(99)]) # wiek
    castrated = models.CharField(max_length=10, choices=CASTRATED_CHOICES, default="") #czy pies jest wykastrowany
    opis = models.TextField(blank = True, null= True) #historia zwierzaka

class Cat(models.Model):

    image = models.ImageField(upload_to='images/', blank=True, null=True) # zdjecie zwierzaka
    name = models.CharField(max_length=60) #imie kota
    rasa_kota = models.CharField(max_length=60, blank=True) # rasa kota
    SIZE = models.CharField(max_length=1, choices=SIZE, default=SIZE[0][0]) #wielkosc kota
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0]) #miesiac dodania ogloszenia
    team = models.CharField(max_length=60, default="") #gotowy do adopcji lub nie 
    age_type = models.CharField(max_length=10, choices=AGE_CHOICES, default='age') #wiek typ
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(99)]) # wiek
    castrated = models.CharField(max_length=10, choices=CASTRATED_CHOICES, default="") #czy kot jest wykastrowany
    opis = models.TextField(blank = True, null= True) # hisotria zwierzaka


    def __str__(self):
        if self.age_type == 'puppy' :
            return "Szczeniak"
        if self.age_type == 'kitten' :
            return "Kociak"
        if self.age_type == 'adult' :
            return
        return f"Wiek: {self.age} lat"

    def __str__(self):
        return f'{self.name} {self.image}'
    
class Osoba(models.Model) :
    name = models.CharField(max_length=60)
    team_people = models.CharField(max_length=60, default="") # pracownik czy user zwykly
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Wpisz poprawny adres email")]) # adres email

    def __str__(self):
        return self.name

class Money_collection(models.Model) :
    name = models.CharField(max_length=100) # cel zbiorki 
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    opis = models.TextField(blank = True, null= True) #  opis np dlacego zbieramy po co ?
    price = models.DecimalField(max_digits=10, decimal_places=2) #  ile kasy potrzebujemy  

    def __str__(self):
        return f'{self.name} {self.image}'
    
class Shelter(models.Model):
    name = models.CharField(max_length=100)  
    location = models.CharField(max_length=200, blank=True, null=True) 
    capacity = models.IntegerField(default=0)  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)

    def available_capacity(self):  # ten def robi to ze pokazuje ile mamy klatek dostepnych 
        return self.capacity - self.cages.count()
    
    def __str__(self):
        return f"{self.name} - Wolne miejsce: {self.available_capacity()}"

#teraz najtrudniejsze zadanie zrobic klatki i przypisanie ich 

class Cage(models.Model):
    cage_id = models.CharField(max_length=10, unique=True)  # id klatki
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name="cages")  # polaczenie tego
    dog = models.OneToOneField(
        'Dog',  #  Przypisanie psa
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="dog_cage"
    )
    cat = models.OneToOneField(
        'Cat',  # przypisaniese kota 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="cat_cage"
    )
    #ulepszenie
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)
    
    def is_empty(self): # wolna klatka ?
        return not self.dog and not self.cat
    
    def war(self): # czy nie bedzie wojny ;)
        if self.dog and self.cat:
            raise ValidationError('W klatce nie moze jednoczenie przebywac kot z psem')
        
    def save(self, *args, **kwargs):
        if self.shelter and self.pk is None:  
            self.shelter.capacity -= 1
            self.shelter.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.shelter:
            self.shelter.capacity += 1
            self.shelter.save()
        super().delete(*args, **kwargs)

    
    def __str__(self):
        return f"Klatka {self.cage_id} w {self.shelter.name}"



