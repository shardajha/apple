from django import forms
from home.models import Book,Author,Genre

class BookForms(forms.Form):
    title=forms.CharField(label='Book Name',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name','class':'form-control'}))
    author=forms.ModelChoiceField(
                    queryset=Author.Object.all(),
                    empty_label='Author',, widget=forms.Select(attrs={'name':'author','id':'author',
                    'class':'custom-select'}))
    #summary=forms.CharField(label='Summary',
                       #     widget=forms.textarea(attrs={'placeholder':'Summary','name':'summary',
                        #    'id':'summary','class':'form-control'}))
  #  isbn=forms.CharField(label='ISBN NUMBER',
   #                         widget=forms.TextInput(attrs={'placeholder':'ISBN Number',
    #                        'class':'form-control','name':'isbn','id':'isbn'}))
    genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
                            widget=forms.CheckboxSelectionMultipl)
    purchasedate=forms.DateField(label'',
                            widget=forms.DateInput(attrs={'placeholder':'purchase Date','name':'pur_date','id':'pur_date',
                            'class':'form-control'}))

