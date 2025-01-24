from rest_framework import serializers
from .models import Dog, Cat, User, Money_collection, Shelter, Cage, MONTHS, SIZE, AGE_CHOICES, CASTRATED_CHOICES


#PIES
class DogSerializer(serializers.Serializer):
    # do odczytu 
    id = serializers.IntegerField(read_only = True)
    #wymagane
    name = serializers.CharField(max_length=60,required=True)
    age = serializers.IntegerField(required=True)
    # inne
    image = serializers.ImageField(required=False)
    rasa_psa = serializers.CharField(max_length=60,required=False)
    SIZE = serializers.ChoiceField(choices = SIZE, default = SIZE[0][0])
    month_added = serializers.ChoiceField(choices=MONTHS.choices, default =MONTHS.choices[0][0])
    age_type = serializers.ChoiceField(choices=AGE_CHOICES, default = "age")
    castrated = serializers.ChoiceField(choices= CASTRATED_CHOICES, default="")
    team = serializers.CharField(max_length=60 ,required=False, allow_blank=True, allow_null=True, default = "")
    opis = serializers.CharField(required=False, allow_blank=True, allow_null=True)

# create
    def create(self, validated_data):
        return Dog.objects.create(**validated_data)

#updejty
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.image = validated_data.get('image', instance.image)
        instance.rasa_psa = validated_data.get('rasa_psa', instance.rasa_psa)
        instance.SIZE = validated_data.get('SIZE', instance.SIZE)
        instance.month_added = validated_data.get('month_added', instance.month_added)
        instance.age_type = validated_data.get('age_type', instance.age_type)
        instance.castrated = validated_data.get('castrated', instance.castrated)
        instance.team = validated_data.get('team', instance.team)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance
    
#KOT
class CatSerializer(serializers.Serializer):
    # do odczytu 
    id = serializers.IntegerField(read_only = True)
    #wymagane
    name = serializers.CharField(max_length=60,required=True)
    age = serializers.IntegerField(required=True)
    # inne
    image = serializers.ImageField(required=False)
    rasa_kota = serializers.CharField(max_length=60,required=False)
    SIZE = serializers.ChoiceField(choices = SIZE, default = SIZE[0][0])
    month_added = serializers.ChoiceField(choices=MONTHS.choices, default =MONTHS.choices[0][0])
    age_type = serializers.ChoiceField(choices=AGE_CHOICES, default = "age")
    castrated = serializers.ChoiceField(choices= CASTRATED_CHOICES, default="")
    team = serializers.CharField(max_length=60 ,required=False, allow_blank=True, allow_null=True, default = "")
    opis = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Cat.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.image = validated_data.get('image', instance.image)
        instance.rasa_kota = validated_data.get('rasa_kota', instance.rasa_kota)
        instance.SIZE = validated_data.get('SIZE', instance.SIZE)
        instance.month_added = validated_data.get('month_added', instance.month_added)
        instance.age_type = validated_data.get('age_type', instance.age_type)
        instance.castrated = validated_data.get('castrated', instance.castrated)
        instance.team = validated_data.get('team', instance.team)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance
    
#USER
class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'name', 'team_people','email']
    read_only_fields = ['id']

#ZBIORKA
class Money_collectionSerializer(serializers.ModelSerializer):
    model = Money_collection
    fields = ['id', 'name', 'image', 'opis', 'price']
    read_only_fields = ['id']

# schronisko 
class ShelterSerializer(serializers.ModelSerializer):
    model = Shelter
    fields = ['id', 'name', 'location', 'capacity', 'created', 'updated']
    read_only_fields = ['id']

#klatka
class CageSerializer(serializers.ModelSerializer):
    model = Cage
    fields = ['id', 'cage_id', 'cat', 'dog', 'shelter', 'created', 'updated']
    read_only_fields = ['id']



    




    




    