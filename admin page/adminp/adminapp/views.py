from django.shortcuts import render,redirect
from . models import User,Details
from . forms import UserRegistration
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os
# Create your views here.
#ds


def home(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_admin =User.objects.filter(email=email,password=password)
        if check_admin:
            request.session['user']="hello admin"
            if 'user' in request.session:
                current_admin =request.session['user']
                data = {"data":current_admin}
                info = Details.objects.all()
            return render(request,'home.html',{'data':data,'info':info})
        else:
            return render(request,'index.html')
    return render(request,'index.html')
    
    

def index(request):
    return render(request,'index.html')


# @login_required(login_url="index")

def insert(request):
    if request.method=="POST":
        name= request.POST['name']
        image = request.FILES['image']
        description = request.POST['description']
        datas = Details(name=name,image=image,description=description)
        datas.save()
        request.session['user']="hello admin"
        if 'user' in request.session:
            current_admin =request.session['user']
            data = {"data":current_admin}
            info = Details.objects.all()
            return render(request,'home.html',{'data':data,'info':info})
    else:
        info =Details.objects.all()
    return render(request,'home.html',{"info":info})



def logout(request):
    try:
        request.session['user']
    except:
        return redirect('index')
    
    return redirect('index')



def delete_data(request,id):
    if 'user' in request.session:
        current_admin =request.session['user']
        data = {"data":current_admin}
        datas =Details.objects.get(pk=id)
        datas.delete()
        info = Details.objects.all()
    return render(request,"home.html",{"info":info,'data':data})
   



# @login_required(login_url="index")
def update_data(request,id):
    update = Details.objects.get(pk=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(update.image)>0:
                os.remove(update.image.path)
            update.image=request.FILES['image'] 
        update.name=request.POST.get('name')
        update.description=request.POST.get('description')
        update.save()
        messages.success(request,"updated successfully")
        request.session['user']="hello admin"
        if 'user' in request.session:
            current_admin =request.session['user']
            data = {"data":current_admin}
            info = Details.objects.all()
            return render(request,'home.html',{'data':data,'info':info})
        # info = Details.objects.all()
        # return render(request,'home.html',{'info':info,'data':data})
    context = {'update':update}
    return render(request,"edit.html",context)

  
def image_list(request):
    request.session['user']="hello admin"
    if 'user' in request.session:
            current_admin =request.session['user']
            data = {"data":current_admin}
            info = Details.objects.all()
            return render(request,'image.html',{'data':data,'info':info})
    else:

        return render(request,'image.html')


def individual_details(request,id):
    request.session['user']="hello admin"
    if 'user' in request.session:
            current_admin =request.session['user']
            data = {"data":current_admin}
    show = Details.objects.get(pk=id)
    return render(request,'ind_details.html',{"info":show,'data':data})
