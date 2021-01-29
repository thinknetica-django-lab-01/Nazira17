from django.shortcuts import render
from .models import Customer


# def home(request):
#     return render(request, 'hello.html')


def user(request):
    context = {
        'customers': Customer.objects.filter(user=request.user),
    }
    return render(request, 'new.html', context)


def home(request):
    turn_on_block = True
    context = {
        'customers': Customer.objects.filter(user=request.user),
        'turn_on_block': turn_on_block
    }
    return render(request, 'hello.html', context)
