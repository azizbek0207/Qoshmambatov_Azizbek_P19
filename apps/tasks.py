from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse

from root import settings


@shared_task
def send_message(msg):
    emails = User.objects.values_list('email', flat=True)
    for email in emails:
        send_mail('python', msg, settings.EMAIL_HOST_USER, [email])
    return f'Ketti'
