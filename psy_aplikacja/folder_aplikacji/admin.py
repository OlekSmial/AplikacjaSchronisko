from django.contrib import admin

# Register your models here.
from .models import Team, Dog, Cat

admin.site.register(Team)
admin.site.register(Dog)
admin.site.register(Cat)