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
        
        file_upload = request.FILES['myfile']
        file_name = file_upload.name
        with open('media/' + file_name , 'wb+') as destination: # MEDIA / 28MALL 
            for chunk in file_upload.chunks():
                destination.write(chunk)

        category_name = request.POST.get('category_name')
        name = request.POST.get('name')
        description = request.POST.get('description')
        return HttpResponse(" File Uploaded " )

    return render(request,'NewsUpload.html')