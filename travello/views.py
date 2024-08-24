from django.shortcuts import render,redirect
from .models import destination, news,footer,slider,Newslettersubscribsion,travel_cnt



# Create your views here.

def index(request):
    
    descs = destination.objects.all()
    newses = news.objects.all()
    footeres = footer.objects.all()
    slideres = slider.objects.all()
    
    
    return render(request, 'index.html', {'descs': descs, 'newses': newses, 'footeres': footeres, 'slideres':slideres})
 
 

def subscribe_view(request):
    if request.method == 'POST':
        newsletter_input_name = request.POST['newsletter_input_name']
        newsletter_input_email = request.POST['newsletter_input_email']
        
        subcribtion =Newslettersubscribsion(name=newsletter_input_name, email=newsletter_input_email)
        subcribtion.save()
        return redirect('/')
    else:
        print('do not matching')
    return render(request,'index.html')  

def contracts(request):
    
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        address = request.POST['address']
        
        tvl_cnt = travel_cnt(name=name, email=email, number=number, address=address )
        tvl_cnt.save()
      
        
    return render(request, 'contract.html')