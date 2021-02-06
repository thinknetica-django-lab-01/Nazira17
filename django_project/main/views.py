from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.views.generic.edit import UpdateView, CreateView
from .forms import UserProfileForm, ProductCreateForm


class CustomerUpdate(UpdateView):
    model = Customer
    form_class = UserProfileForm
    template_name = 'update.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return '/goods'


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        
        product_list = Product.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context['paje_obj'] = page_obj
        context['page_number'] = int(page_number)
        context['paginator'] = paginator
        return context

    def get_queryset(self):
        queryset = super(ProductList, self).get_queryset()
        query = self.request.GET.get('tag')
        if query:
            object_list = queryset.filter(tag__name=query)
        else:
            object_list = queryset
        return object_list


class ProductDetailView(DetailView):
    template_name = 'product-detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    context_object_name = 'products'
    template_name = 'product-add.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    context_object_name = 'products'
    template_name = 'product-add.html'


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
