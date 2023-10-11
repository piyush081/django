from django.shortcuts import render,redirect
from .models import *



def home(request):
    if request.method =='POST':
        return render(request,'home.html')

def payment(request):
    if request.method =='POST':
        return redirect('/payment/')
    


def index(request):
  if request.method =='POST':
    name = request.POST.get('name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phoneno')
    password = request.POST.get('password')

    data= test.objects.create(username=username, email=email, phone=phone, password=password,student_name=name)
    data.save()
    
    return redirect('/login/')
  return render(request,'index.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email'] 
        password = request.POST['password'] 
        user=test.objects.get(email=email, password=password) 
        if user:
           return redirect('/hello/') 
        else:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')








