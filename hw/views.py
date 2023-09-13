from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from hw.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'description', 'category', 'price', 'image')
    success_url = reverse_lazy('hw:index')


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Список продуктов'
        return context


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('title', 'description', 'category', 'price', 'image')
    success_url = reverse_lazy('hw:index')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('hw:index')


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'hw/contact.html', context)
