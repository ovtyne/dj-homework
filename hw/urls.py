from django.urls import path
from django.views.decorators.cache import cache_page

from hw.apps import HwConfig
from hw.views import contact, ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView, CategoryListView

app_name = HwConfig.name

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('detail_view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='detail_view'),
    path('', ProductListView.as_view(), name='index'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('add_version/<int:pk>', VersionCreateView.as_view(), name='add_version'),
    path('contact/', contact, name='contact'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]
