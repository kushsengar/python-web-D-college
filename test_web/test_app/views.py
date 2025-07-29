from django.shortcuts import render , HttpResponse , redirect
from test_app.models import test

# Create your views here.

def home(request):
    
    return render(request,"home.html")  

def aboutUs(request):
    return render(request , "aboutUs.html")

def contact_us(request):
    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('number')

        test_instance = test(name=var1 , number = var2)
        test_instance.save()
        return redirect('home')
    return render(request ,"contact_us.html")

