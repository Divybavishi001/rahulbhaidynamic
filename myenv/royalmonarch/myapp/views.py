from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def knowledge(request):
    return render(request, 'knowledge.html')
from django.conf import settings

@api_view(["POST"])
def check_mail(request):
    from django.core.mail import send_mail
    send_mail(
        'Check mail',
        ' checking....',
        settings.EMAIL_HOST_USER,
        ['bavishidivy@gmail.com'],
        fail_silently=False
    )
    send_mail(
        'Repling mail',
        'Thank you for your time',
        'bavishidivy@gmail.com',
        [settings.EMAIL_HOST_USER],
        fail_silently=False
    )
    print('message pass')
    return JsonResponse({"Status":True})

