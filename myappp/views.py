from django.http import HttpResponse
from django.shortcuts import render
from .models import register
import sqlite3
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request,'index.html')
    

def salam(request):
    return HttpResponse(" Salam ")

def registerfunc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        register.objects.create(name = name , email = email , password = password)

    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 

        print(email)
        print(password)
        
        conn = sqlite3.connect("db.sqlite3") # Database e qosul

        cur = conn.cursor() # Database ucun cursor yarat

        cur.execute("SELECT * FROM myappp_register WHERE Email = ?", (email,))

        row = cur.fetchone()
        row_list = list(row)

        if password in row_list:
            context = {
                "email" : email,
            }

        else :
            return redirect("/Login")


    return render(request,"login.html")
