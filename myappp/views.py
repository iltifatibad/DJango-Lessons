from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import sqlite3
from django.shortcuts import redirect
# Create your views here.

def index(request):

    conn = sqlite3.connect("db.sqlite3") # DataBase e qosul

    cur = conn.cursor() # Database ucun cursor yarat

    cur.execute(" SELECT * FROM myappp_news_data ORDER BY RANDOM() LIMIT 1 ") # select * from myappp_register where email = iltifatibad@gmail.com 

    row = cur.fetchone()

    row_list = list(row)
    
    # [1, 'media/Photo.jpg', 'Forest', 'Mountains', 'Beauty Of Mountains']
    #  0,      1                 2          3                4
    context = {
            "img_path" : row_list[1], # img_path = /media/Photo.jpg
            "category_name" : row_list[2],
            "img_name" : row_list[3],
            "description" : row_list[4]
    }

    return render(request,'index.html',context)
    

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
        email = request.POST.get('email') # iltifatibad@gmail.com
        password = request.POST.get('password') 
        
        conn = sqlite3.connect("db.sqlite3") # Database e qosul # Conn = Connection

        cur = conn.cursor() # Database ucun cursor yarat

        cur.execute("SELECT * FROM myappp_register WHERE Email = ?", (email,)) # select * from myappp_register where email = iltifatibad@gmail.com 

        row = cur.fetchone() # Tuple Type (1, iltifat, iltifatibad@gmail.com , 12345)
        row_list = list(row)  # [ id : name : email : password ] [ 1, iltifat, iltifatibad@gmail.com , 12345 ]

        if password in row_list:
            context = {
                "name" : row_list[1], # name = iltifat
            }

            return render(request, 'index.html', context)
            # return HttpResponse(request,"index.html",context)

        else :
            return redirect("/Login")


    return render(request,"login.html")


# --------------------------------------------------------------------------------------------------------


def newsupload(request):

    if request.method == 'POST' and 'myfile': # Multi Part Forms
        category_name = request.POST.get('category_name')
        name = request.POST.get('name')
        description = request.POST.get('Description')

        file_upload = request.FILES['myfile']
        file_name = file_upload.name # Faylin Adi 
        img_path = 'media/' + file_name
        with open(img_path, 'wb+') as destination: # MEDIA / 28MALL 
            for chunk in file_upload.chunks():
                destination.write(chunk)

        news_data.objects.create(img_path = img_path, category_name = category_name, name = name, description = description)
        
        
        return HttpResponse(" File Uploaded " )

    return render(request,'NewsUpload.html')