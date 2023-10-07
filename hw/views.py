import os
from dotenv import load_dotenv

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from config.settings import BASE_DIR
from hw.forms import ProductForm, VersionForm
from hw.models import Product, Version, Category
from hw.services import get_categories_from_cache

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('hw:index')

    def form_valid(self, form):
        product = form.save()
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список продуктов'
        aaa = os.getenv('IS_NOT_AUTH_ACCESS') == 'True'
        context['not_auth_access'] = aaa

        for product in context['object_list']:
            active_version = product.version_set.filter(is_current=True).first()
            if active_version:
                product.active_version_number = active_version.number
                product.active_version_name = active_version.name
            else:
                product.active_version_number = None
                product.active_version_name = None

        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('hw:index')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('hw:index')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('hw:index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление версии продукта'

        return context


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'

        categories = get_categories_from_cache()
        context['categories'] = categories

        return context


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'hw/contact.html', context)
