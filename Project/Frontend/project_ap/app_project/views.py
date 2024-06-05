from django.shortcuts import render
from django.http import JsonResponse
import requests

def register_user(request):
    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        response = requests.post('http://localhost:8000/register/', json=data)
        return JsonResponse(response.json())
    else:
        return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        response = requests.post('http://localhost:8000/login/', json=data)
        return JsonResponse(response.json())
    else:
        return render(request, 'index.html')
