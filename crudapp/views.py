from django.shortcuts import render,redirect
from .models import crStudent
from django.contrib import messages
from django.db.models import Q 
# Create your views here.

def crudStudent(request):
    
    crdts = crStudent.objects.all()
    # for search button 
    query= ''   
    if request.method =='POST':
        # name = request.POST['name']
        # email = request.POST['email']
        
        # crst = crStudent(name=name, email=email)
        # crst.save()
        # messages.success(request,'Student added successfully')
        # return redirect('/crudapp/')
        
        if 'add' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            crStudent.objects.create(name=name, email=email)
            messages.success(request,'Student added successfully')
            return redirect('/crudapp/')
    
        elif 'update' in request.POST:
            id = request.POST.get('id')    
            name = request.POST.get('name')
            email = request.POST.get('email')
            
            update_student = crStudent.objects.get(id=id)
            update_student.name = name
            update_student.email = email
            update_student.save()
            messages.success(request, 'Student updated successfully')
            return redirect('/crudapp/')
        
        elif 'delete' in request.POST:
            id = request.POST.get('id')
            crStudent.objects.get(id=id).delete()
            messages.success(request, 'Student deleted successfully')
            return redirect('/crudapp/')
            
        elif 'search' in request.POST:
            query =request.POST.get('searchquery')
            crdts = crStudent.objects.filter(Q(name__icontains=query)  | Q(email__icontains=query))
 
    return render(request, 'crdstudent/index.html',{'crdts':crdts, 'query': query})