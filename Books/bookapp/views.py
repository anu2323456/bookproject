
from django.shortcuts import render, redirect

from bookapp.forms import Form
from bookapp.models import Books


# Create your views here.
def index(request):
    bk=Books.objects.all()
    return render(request,'index.html',{'b':bk})

def detail(request,id):
    book=Books.objects.get(id=id)
    return render(request,'detail.html',{'books':book})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year=request.POST.get('year')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        Books.objects.create(name=name,year=year,desc=desc,img=img)
        return redirect('/')
    return render(request,'add.html')


def update(request,id):
    I=Books.objects.get(id=id)
    forms=Form(request.POST,None,request.FILES,instance=I)
    if forms.is_valid():
       forms.save()
       return redirect('/')
    return render(request,'edit.html',{'forms':forms,'id':I})

def delete(request,id):
    if request.method=='POST':
        b=Books.objects.get(id=id)
        b.delete()
        return redirect('/')
    return render(request,'delete.html')







