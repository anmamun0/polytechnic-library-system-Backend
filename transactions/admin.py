from django.contrib import admin

# Register your models here.
from .models import Transaction 



class TransactionAdmin(admin.ModelAdmin):
    list_display=['profile_user','book_title','status']

    def book_title(self,obj):
        return obj.book.title
    def profile_user(self,obj):
        return obj.profile.user.username
    
    book_title.short_description = "Book Title"  # Set column name in Django Admin

admin.site.register(Transaction,TransactionAdmin)
 