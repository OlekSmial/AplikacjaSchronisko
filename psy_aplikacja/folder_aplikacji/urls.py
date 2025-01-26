
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dogs/', views.dog_list),
    path('dogs/<int:pk>/', views.dog_detail),
    path('cats/', views.cat_list),
    path('cats/<int:pk>/', views.cat_detail),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('moneys/', views.money_collection_list),
    path('moneys/<int:pk>/', views.money_collection_detail),
    path('shelters/', views.shelter_list),
    path('shelters/<int:pk>/', views.shelter_detail),
    path('cages/', views.cage_list),
    path('cages/<int:pk>/', views.cage_detail),
    path('welcome/', views.welcome_view),
    path('dogs_html/', views.dog_list_html),
    path('dogs_html/<int:pk>/', views.dog_detail_html),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #ZDJECIA