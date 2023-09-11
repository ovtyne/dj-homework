from django.shortcuts import render

from hw.models import Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Список продуктов'
    }
    return render(request, 'hw/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'hw/contact.html', context)
