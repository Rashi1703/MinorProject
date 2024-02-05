from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Users
import smtplib
import ssl
from email.message import EmailMessage
# Create your views here.
def index(request):
    return render(request, 'login.html')

def success(request):
    if request.method == 'POST':
        entered_username = request.POST.get('username')
        entered_password = request.POST.get('password')
        Users_registered=Users.objects.filter(username=entered_username,password=entered_password)
        if Users_registered.exists():
            return redirect('choice')
        else:
            return redirect("index")
    return redirect("index")

def signup(request):
    return render(request, 'signup.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        Email = request.POST.get('email')
        Login = Users(username=username,mail=Email, password=password)
        try:
            Login.save()
        except:
            return HttpResponse('404 error')
    return render(request, 'login.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def send_password(request):
    if request.method == 'POST':
        entered_username = request.POST.get('username')
        entered_email = request.POST.get('email')
        Users_registered=Users.objects.filter(username=entered_username,mail=entered_email)
        if Users_registered.exists():
            ob=Users.objects.get(username=entered_username)
            password_tosend=ob.password
            try:
                email_sender = 'rashijain1710@gmail.com'
                email_password = 'fkep hojo abpc hboy'
                email_receiver = entered_email
                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['Subject'] = "Welcome to sentiment analysis"
                em.set_content(str(password_tosend))
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())
            except:
                return redirect("home")


        else:
            return redirect("home")
    return redirect("index")


def choice(request):
    return render(request, 'choice.html')

def AudioBased(request):
    return render(request, 'AudioBased.html')

def TextBased(request):
    return render(request, 'TextBased.html')

def ResultAudio(request):
    return HttpResponse('Audio')

def ResultText(request):
    return redirect('Result')

def Result(request):
    return render(request,'Result.html')