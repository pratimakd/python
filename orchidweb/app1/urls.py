from django.urls import path
from . views import StudentListView
from . views import StudentCreateView
from . views import StudentUpdateView
from . views import StudentDeleteView
from . views import StudentDetailView

from . views import AuthorListView
from . views import AuthorCreateView
from . views import AuthorUpdateView
from . views import AuthorDeleteView
from . views import AuthorDetailView

from . views import ProductListView
from . views import ProductCreateView
from . views import ProductUpdateView
from . views import ProductDeleteView
from . views import ProductDetailView


app_name='app1'
from . import views
urlpatterns=[
       # path('index',views.IndexView.as_view(),name='index'),
       # path('today',views.IndexView.as_view(),name='today'),
        #path('form',views.IndexView.as_view(),name='form'),
        path('student',StudentListView.as_view(),name='student'),
        path('student/create',StudentCreateView.as_view(),name='student-create'),
        path('student/update/<pk>',StudentUpdateView.as_view(),name='student-update'),
        path('student/delete/<pk>',StudentDeleteView.as_view(),name='student-delete'),
        path('student/detail/<pk>',StudentDetailView.as_view(),name='student-detail'),

        path('author',AuthorListView.as_view(),name='author'),
        path('author/create',AuthorCreateView.as_view(),name='author-create'),
        path('author/update/<pk>',AuthorUpdateView.as_view(),name='author-update'),
        path('author/delete/<pk>',AuthorDeleteView.as_view(),name='author-delete'),
        path('author/detail/<pk>',AuthorDetailView.as_view(),name='author-detail'),

        path('product',ProductListView.as_view(),name='product'),
        path('product/create',ProductCreateView.as_view(),name='product-create'),
        path('product/update/<pk>',ProductUpdateView.as_view(),name='product-update'),
        path('product/delete/<pk>',ProductDeleteView.as_view(),name='product-delete'),
        path('product/detail/<pk>',ProductDetailView.as_view(),name='product-detail'),
        
]
