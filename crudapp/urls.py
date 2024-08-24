from django.urls import path
from .views import crudStudent


urlpatterns = [
    
    path('', crudStudent, name='crudStudent'),

    
]