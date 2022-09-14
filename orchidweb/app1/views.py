from django.views.generic import ListView, CreateView, UpdateView,DeleteView, DetailView

from .models import Student
from .form import StudentForm

from .models import Author
from .form import AuthorForm

from .models import Product
from .form import ProductForm

from django.urls import reverse_lazy
#class IndexView(TemplateView):
    #template_name="hello/index.html"
    #template_name="hello/today.php"
    #template_name="hello/form.html"
# Create your views here.
class StudentListView(ListView):
    template_name="hello/student/student.html"
    model=Student

class StudentCreateView(CreateView):
    template_name="hello/student/form.html"
    form_class= StudentForm
   # success_url='/hello/student'
    success_url=reverse_lazy('app1:student')

class StudentUpdateView(UpdateView):
    template_name="hello/student/form.html"
    form_class= StudentForm
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:student') #(key:value)
    model=Student

class StudentDeleteView(DeleteView):

    template_name="hello/student/delete.html"
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:student') #(key:value)
    model=Student

class StudentDetailView(DetailView):

    template_name="hello/student/detail.html"
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:student') #(key:value)
    model=Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['students']="this is the list of students"
        #context['students']=Student.objects.filter(present=True)\
        context['all_students']=Student.objects.all()
        
        return context
    

class AuthorListView(ListView):
    template_name="hello/author/author.html"
    model=Author

class AuthorCreateView(CreateView):
    template_name="hello/author/form.html"
    form_class= AuthorForm
   # success_url='/hello/student'
    success_url=reverse_lazy('app1:author')

class AuthorUpdateView(UpdateView):
    template_name="hello/author/form.html"
    form_class= AuthorForm
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:author') #(key:value)
    model=Author

class AuthorDeleteView(DeleteView):

    template_name="hello/author/delete.html"
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:author') #(key:value)
    model=Author

class AuthorDetailView(DetailView):

    template_name="hello/author/detail.html"
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:author') #(key:value)
    model=Author

class ProductListView(ListView):
    template_name="hello/author/author.html"
    model=Author

class ProductCreateView(CreateView):
    template_name="hello/product/form.html"
    form_class= ProductForm
   # success_url='/hello/student'
    success_url=reverse_lazy('app1:product')

class ProductUpdateView(UpdateView):
    template_name="hello/product/form.html"
    form_class= ProductForm
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:product') #(key:value)
    model=Product

class ProductDeleteView(DeleteView):

    template_name="hello/product/delete.html"
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:product') #(key:value)
    model=Product

class ProductDetailView(DetailView):

    template_name="hello/product/detail.html"
   # success_url="/app1/student" #name of the app/url path name
    success_url=reverse_lazy('app1:product') #(key:value)
    model=Product


