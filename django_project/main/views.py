from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product.html'


class ProductDetailView(DetailView):
    template_name = 'product-detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)


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
