from django.contrib import admin

# Register your models here.
from .models import Dog, Cat, User, Money_collection, Shelter, Cage

# ADMIN ROZPISKA

class DogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rasa_psa', 'SIZE']  
    search_fields = ['id']
    list_filter = ['SIZE', 'castrated', 'age', 'rasa_psa']  

class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rasa_kota', 'SIZE']  
    search_fields = ['id']
    list_filter = ['SIZE', 'castrated', 'age', 'rasa_kota']   

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'team_people', 'email']  
   
class MoneyCollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']  
    list_filter = ['price']  

class ShelterAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity']  
    list_filter = ['capacity']  

class CageAdmin(admin.ModelAdmin):
    list_display = ['cage_id', 'shelter', 'dog', 'cat']    
    list_filter = ['shelter']  


admin.site.register(Dog, DogAdmin)
admin.site.register(Cat, CatAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Money_collection, MoneyCollectionAdmin)
admin.site.register(Shelter, ShelterAdmin)
admin.site.register(Cage, CageAdmin)
