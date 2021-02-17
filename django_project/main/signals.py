from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='common users'))


@receiver(user_signed_up)
def send_welcome_email(user, **kwargs):
    subject = 'Registration Confirmation'
    message = render_to_string('account/email/welcome.html', {
        'name': user.username,
    })
    text_content = render_to_string("account/email/welcome.txt", {"name": user.username})
    email = EmailMultiAlternatives(subject, text_content, from_email='nazira.yegizbayeva@gmail.com', to=[user.email])
    email.attach_alternative(message, 'text/html')
    email.send()
