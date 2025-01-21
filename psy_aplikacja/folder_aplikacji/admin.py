from django.contrib import admin

# Register your models here.
from .models import Dog, Cat, User, Money_collection, Shelter, Cage

admin.site.register(Dog)
admin.site.register(Cat)
admin.site.register(User)
admin.site.register(Money_collection)
admin.site.register(Shelter)
admin.site.register(Cage)
