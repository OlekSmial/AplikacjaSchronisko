from django.contrib import admin

# Register your models here.
from .models import Team, Dog

admin.site.register(Team)
admin.site.register(Dog)