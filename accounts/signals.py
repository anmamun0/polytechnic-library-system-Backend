from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# @receiver(post_save, sender=Profile)
# def print_profile_fields(sender, instance, created, **kwargs):
#     if created:
#         context = {}
#         for field in instance._meta.fields:
#             field_name = field.name
#             value = getattr(instance, field_name)
#             context[field_name] = value 
#         body = render_to_string('templates/registrations_received.html',context) # Adds alternative HTML content 

#         email = EmailMultiAlternatives(
#             subject="Registration Received – Pending Verification",
#             body='',
#             from_email= 'SPI Libary <noreply@example.com>', 
#             to = [context.email],
#         )
#         email.attach_alternative(body, "text/html")
#         email.send()
