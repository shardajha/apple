from django import forms
from home.models import Book,Author,Genre

class BookForms(forms.Form):
    title=forms.CharField(label='Book Name',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name','class':'form-control'}))
    author=forms.ModelChoiceField(
                    queryset=Author.objects.all(),
                    empty_label='Author', widget=forms.Select(attrs={'name':'author','id':'author',
                    'class':'custom-select'}))
    purchasedate=forms.DateField(label='',
                            widget=forms.DateInput(attrs={'placeholder':'purchase Date','name':'pur_date','id':'pur_date',
                            'class':'form-control'}))
    # genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
    #                         widget=forms.CheckboxSelectionMultipl)
#     summary=forms.CharField(label='Summary',
#                            widget=forms.textarea(attrs={'placeholder':'Summary','name':'summary',
#                            'id':'summary','class':'form-control'}))
#    isbn=forms.CharField(label='ISBN NUMBER',
#                            widget=forms.TextInput(attrs={'placeholder':'ISBN Number',
#                            'class':'form-control','name':'isbn','id':'isbn'}))



# from django import forms

# class CustomForms(forms.Form):
#     username = forms.CharField(
#         label = 'usename',
#         widget = forms.TextInput(
#             attrs = {'placeholder':'Your username','class':'form-control','max':'20'
#             }
#         )
#     )


#     email = forms.EmailField(label='Your Email',widget=forms.EmailInput(attrs={'placeholder':'ac@gmail.com','class':'form-control'}))               