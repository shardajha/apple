from django.shortcuts import render
from  home.forms import BookForms
from home.models import Book
from home.html import Book

# Create your views here.


def form_view(request):
    msg=''
    if request.method=='POST':
        form=BookForms(request.POST)
        if form.is_valid():
            book=Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('pur_date'),
                genre=form.cleaned_data.get('genre'),
                author=form.cleaned_data.get('author')
            )
            book.save()
            msg='Book Added Successfully!!!'
        else:
                msg=form.errors
    else:
        form=BookForms()
    return render(request,'forms2.html',{"msg":msg,"forms":form})


def model_view(request):
    msg=''
    if request.method=='POST':
        form=BookForms(request.POST)
        if form.is_valid():
            form.save()
            msg='Book Added Successfully!!!'
        else:
                msg=form.errors
    else:
        form=ModelBookForms()
    return render(request,'forms2.html',{"msg":msg,"forms":form})

def html_view(request):
    value=''
    if request.method=='POST':
        value==request.POST.get('name')
        return render(request,'values.html',{'value':value})
    else:
        value='Worng InputS'
        
        return render(request,'design.html')




