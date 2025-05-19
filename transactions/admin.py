from django.contrib import admin

# Register your models here.
from .models import Transaction 



class TransactionAdmin(admin.ModelAdmin):
    list_display=['user_username','book_title','status']

    def book_title(self,obj):
        return obj.book.title
    def user_username(self,obj):
        return obj.user.username
    
    book_title.short_description = "Book Title"  # Set column name in Django Admin

admin.site.register(Transaction,TransactionAdmin)
 