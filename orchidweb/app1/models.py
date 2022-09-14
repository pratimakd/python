from django.db import models

class Student(models.Model):
    name= models.CharField(max_length=200,null=True)
    age= models.IntegerField()
    present= models.BooleanField()
    
    def __str__(self):
        return self.name +'Age:'+str(self.age)

class Author(models.Model):
    position= models.CharField(max_length=200,null=True)
    experience= models.IntegerField()
    active= models.BooleanField()
    def __str__(self):
        return self.position +'Experience:'+str(self.experience)

class Product(models.Model):
    title= models.CharField(max_length=500)
    price= models.IntegerField()
    desc=models.TextField()
    is_active= models.BooleanField(default=False)
    created_date=models.DateTimeField()
    url=models.URLField()
    email=models.EmailField()
    #image=models.ImageField()

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'

    def __str__(self):
        return self.title +'Price:'+str(self.price)
    

# Create your models here.
