from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Users
# Create your views here.
def index(request):
    return render(request, 'login.html')

def success(request):
    if request.method == 'POST':
        entered_username = request.POST.get('username')
        entered_password = request.POST.get('password')
        Users_registered=Users.objects.filter(username=entered_username,password=entered_password)
        if Users_registered.exists():
            return HttpResponse('success')
        else:
            return redirect("index")
    return redirect("index")

def signup(request):
    return render(request, 'signup.html')

