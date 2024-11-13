from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import sqlite3
from django.shortcuts import redirect
# Create your views here.

def index(request):

    myimg = []   #[media/Photo.jpg, media/Photo2.jpg, media/Photo3.jpg]
    myname = []     #[Forest, Forest2, Forest3]
    mytopic = []  #[Mountains, Mountains2, Mountains3]
    mydesc = []   #[Beauty Of Mountains, Beauty Of Mountains2, Beauty Of Mountains3]


    conn = sqlite3.connect("db.sqlite3") # DataBase e qosul

    cur = conn.cursor() # Database ucun cursor yarat

    for i in range (1 , 7): # i = 1
            cur.execute(" SELECT * FROM myappp_news_data ORDER BY RANDOM() LIMIT 1 ") # select * from myappp_register where email = iltifatibad@gmail.com 
    
            # (1, 'media/Photo.jpg', 'Forest', 'Mountains', 'Beauty Of Mountains') # Tuple 
            # (2, 'media/Photo2.jpg', 'Forest2', 'Mountains2', 'Beauty Of Mountains2') # Tuple 
            # (3, 'media/Photo3.jpg', 'Forest3', 'Mountains3', 'Beauty Of Mountains3') # Tuple 

            row = cur.fetchone()x

            row_list = list(row)  
            
            myimg.append(row_list[1])
            myname.append(row_list[2])
            mytopic.append(row_list[3])
            mydesc.append(row_list[4])
            
    

    
    context = {
            "img_path" : myimg,
            "category_name" :myname,
            "img_name" : mytopic,
            "description" : mydesc
    }

    print(myimg)
    print(myname)
    print(mytopic)
    print(mydesc)

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