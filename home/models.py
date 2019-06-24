from django.db import models
import uuid
# from .forms import BookForms
# from .models import Book

# Create your models here.

class Book(models.Model):
    id = models.UUIDField('Book ID', primary_key=True, default = uuid.uuid4,help_text="Generated unique id for the book")
    name=models.CharField(max_length = 100, help_text = 'Book_Name',null=True)
    purchase_date=models.DateField(null=True, blank = True)
    genre=models.ManyToManyField('Genre',help_text='Genre of the book.')
    author=models.ForeignKey('Author', on_delete=models.SET_NULL,help_text='Book Author',null=True)
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Author(models.Model):
    id=models.AutoField(primary_key=True)
    author_name=models.CharField(max_length=100,help_text='Author Name',null=True)
    numChoice=(
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5','Five')
    )
    total_books_written=models.CharField(max_length=1,choices=numChoice, blank=True)
    date_of_birth = models.DateField('Birth',null=True, blank=True)
    date_of_death = models.DateField('Death',null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author_name

class Genre(models.Model):
    genre=models.CharField(max_length=100,help_text='Genre', null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genre

class Issue(models.Model):
    name=models.CharField(max_length = 100, help_text = 'Book_Name',null=True)
    numChoice=(
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5','Five')
    )
    total_books_taken=models.CharField(max_length=1,choices=numChoice, blank=True)
    issue_take=models.DateTimeField('Issued',null=True,blank=True)
    issue_return=models.DateTimeField('Return',null=True,blank=True)
    
    def __str__(self):
        return self.name