# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction
from datetime import timedelta

# @receiver(post_save, sender=Transaction)
# def set_return_date(sender, instance, created, **kwargs):
#     if created and instance.due_date:
#         instance.return_date = (instance.borrow_date + timedelta(days=instance.due_date)).date()
#         instance.save()
