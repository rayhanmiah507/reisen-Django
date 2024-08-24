from django.urls import path
from .views import index,subscribe_view,contracts

urlpatterns = [
    path('', index, name='index'),
    path('subscribe/', subscribe_view, name='subscribe_view'),
    path('contact/', contracts, name='contracts'),
   
    
]