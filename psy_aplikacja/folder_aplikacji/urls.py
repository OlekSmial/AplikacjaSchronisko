
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dogs/', views.dog_list),
    path('dogs/<int:pk>/', views.dog_detail),
    path('cats/', views.cat_list),
    path('cats/<int:pk>/', views.cat_detail),
    path('users/', views.user_list),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)