from django.db.models.signals import post_save, pre_save,post_delete
from django.dispatch import receiver
import uuid
import os
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from account.models import Customer
from products.models import ProductImage
from shop.models import Brand,Category


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


@receiver(post_delete, sender=Brand)
@receiver(post_delete, sender=Category)
@receiver(post_delete, sender=ProductImage)
@receiver(post_delete, sender=Customer)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            


@receiver(pre_save, sender=Brand)
@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=ProductImage)
@receiver(pre_save, sender=Customer)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)