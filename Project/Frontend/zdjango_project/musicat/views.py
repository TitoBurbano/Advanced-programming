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

        # Crear el payload en formato JSON
        payload = {
            "username": username,
            "password": password
        }

        # Enviar la solicitud al servicio web FastAPI para la autenticación
        response = requests.post("http://localhost:8000/login", json=payload)
        
        if response.status_code == 200 and response.text == "Login successful":
            # Si el inicio de sesión es exitoso, redirige a la página 'home'
            return redirect('home')
        else:
            # Si las credenciales son inválidas, muestra un mensaje de error en la misma página de inicio de sesión
            return render(request, 'login.html', {'message': 'Invalid username or password'})
    else:
        # Si no se ha enviado el formulario, simplemente renderiza la página de inicio de sesión
        return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')