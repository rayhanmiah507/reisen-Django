from django.shortcuts import render,redirect
from .models import add_students
# Create your views here.

def home(request):
    
    stdn = add_students.objects.all()
    
    return render(request,'studentm/home.html', {'stdn': stdn})

def add_student(request):
    
    if request.method == 'POST':
        roll = request.POST['roll']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        
        student_add = add_students(roll=roll, name=name, email=email, address=address, phone=phone)
        student_add.save()
        
        return redirect('/student/')  
    else:  
        print('do not working')
    return render(request, 'studentm/add_std.html')

def delete_std(request,roll):
    
    s = add_students.objects.get(pk=roll)
    s.delete()
    return redirect('/student/')

def update_std(request,roll):
    
    sts = add_students.objects.get(pk=roll)
    return render(request,'studentm/updates.html',{'sts':sts})

def updatesData(request,roll):
    
    std_roll = request.POST.get('std_roll')
    std_name = request.POST.get('std_name')
    std_email = request.POST.get('std_email')
    std_address = request.POST.get('std_address')
    std_phone = request.POST.get('std_phone')
    
    sts = add_students.objects.get(pk=roll)
    
    sts.roll = std_roll
    sts.name = std_name
    sts.email = std_email
    sts.address = std_address
    sts.phone = std_phone
    
    sts.save()
    return redirect('/student/')