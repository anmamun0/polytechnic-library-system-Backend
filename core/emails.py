from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


def Registration_received(user,profile): 
    try:
        context = {} 
        for field in profile._meta.fields:
            field_name = field.name
            field_value = getattr(profile, field_name)
            context[field_name] = field_value  

        body = render_to_string('registrations_received.html', context)

        email = EmailMultiAlternatives(
        subject="Registration Received – Pending Verification",
            body='',
            from_email= 'SPI Libary <noreply@example.com>', 
            to = [profile.email],
        )
        email.attach_alternative(body, "text/html")
        email.send()
    except Exception as e:
        print('Email send error :', str(e))
        

def Account_verified(user,profile): 
    try:
        context = {
            'id' : profile.id,
            'full_name':profile.full_name 
        }  

        body = render_to_string('account_verified.html', context)

        email = EmailMultiAlternatives(
        subject="Verification Successfull",
            body='',
            from_email= 'SPI Libary <noreply@example.com>', 
            to = [profile.email],
        )
        email.attach_alternative(body, "text/html")
        email.send()
    except Exception as e:
        print('Email send error :', str(e))