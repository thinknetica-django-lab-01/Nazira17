from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from .models import *
from django.template.loader import render_to_string
from datetime import datetime, timedelta


@shared_task
def send_new_good():
    subscribers = Subscriber.objects.values("subscriber__email")
    today = datetime.today()
    products = Product.objects.filter(add_date__lte=today, add_date__gt=today - timedelta(days=7))
    subject = 'Check out the new product'
    message = render_to_string('account/email/new_good.html', {
        'product': products,
        'name': Subscriber.subscriber,
    })
    text_content = render_to_string("account/email/new_good.txt", {"name": Subscriber.subscriber})
    email = EmailMultiAlternatives(subject, text_content, from_email='nazira.yegizbayeva@gmail.com',
                                   to=[subscribers])
    email.attach_alternative(message, 'text/html')
    email.send()
