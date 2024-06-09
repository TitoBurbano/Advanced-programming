from django.shortcuts import render, redirect
import requests 
# Create your views here.

# musicat/views.py

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        payload = {
            "username": username,
            "password": password
        }


        response = requests.post("http://localhost:8000/login", json=payload)
        
        if response.status_code == 200 and response.text == "Login successful":
            
            return redirect('home')
        else:
            
            return render(request, 'login.html', {'message': 'Invalid username or password'})
    else:
        
        return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')