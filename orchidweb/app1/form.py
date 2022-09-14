from django import forms
from .models import Student
from .models import Author
from .models import Product
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','age','present']
class AuthorForm(forms.ModelForm):
     class Meta:
        model=Author
        fields=['position','experience','active']
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['title','price','desc','is_active','created_date','url','email']