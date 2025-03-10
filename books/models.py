from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,blank=True,unique=True,null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    image = models.ImageField(upload_to='books/media/uploads/', null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)  # Unique ISBN number
    category = models.ManyToManyField(Category, blank=True,related_name='books') 
    description = models.TextField() 
    copies = models.IntegerField(default=0)  

    def __str__(self):
        return f"{self.isbn} - {self.title}"
