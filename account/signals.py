from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import uuid
from django.conf import settings
from django.core.mail import send_mail
from .models import Customer
from django.contrib import messages

@receiver(post_save,sender=User)
def send_email_token(sender,instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            email = instance.email
            try :
                subject = "Verify Your Account !"
                email_from = settings.EMAIL_HOST_USER
                message = f'Hi, Click on the link to verify your account http://127.0.0.1:8000/activate/{email_token}'
                send_mail(subject, message, email_from,[email])
                Customer(user_id=instance,token=email_token).save()
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


