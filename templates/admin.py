from django.contrib import admin
from home.models import Book_Name ,Book_Author,Gerne

#Register your models here.

admin.site.register(Book_Name,Book_Author)