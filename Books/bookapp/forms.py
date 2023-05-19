from django import forms
from.models import Books
class Form(forms.ModelForm):
    class Meta:
        fields=['name','year','desc','img']
        model=Books
