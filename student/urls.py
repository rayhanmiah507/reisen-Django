
from django.urls import path
from .views import home,add_student,delete_std,update_std,updatesData

urlpatterns = [
    
    path('', home, name='home'),
    path('std_add/', add_student, name='add_student'),
    path('delete/<int:roll>', delete_std, name='delete_std'),
    path('update/<int:roll>', update_std, name='update_std'),
    path('updatesData/<int:roll>', updatesData, name='updatesData'),
 
    
]