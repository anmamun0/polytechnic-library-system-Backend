from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from datetime import date, timedelta

from .constant import STATUS_CHOICES, STATUS_DUE
  
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    due_date = models.CharField(choices=STATUS_DUE, default=7,null=True,blank=True) 
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='borrowed')
    test = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    # def calculate_fine(self):
    #     if not self.return_date:
    #         return 0  # Not returned yet, can't calculate fine

    #     # Calculate the allowed return date (borrow_date + due_date days)
    #     allowed_return_date = self.borrow_date.date() + timedelta(days=self.due_date)

    #     # If returned late
    #     if self.return_date > allowed_return_date:
    #         days_late = (self.return_date - allowed_return_date).days

    #         # Get the latest fine rate (assumes you want current rate)
    #         latest_fine_rate = FineRate.objects.order_by('-effective_date').first()

    #         if latest_fine_rate:
    #             return days_late * latest_fine_rate.per_day_fine
    #         else:
    #             return 0  # no fine rate set yet
    #     else:
    #         return 0
