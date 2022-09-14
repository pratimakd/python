from django.contrib import admin
from .models import Student
admin.site.register(Student)

from .models import Author
admin.site.register(Author)

from .models import Product
admin.site.register(Product)
# Register your models here.
