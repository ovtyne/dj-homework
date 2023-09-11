from django.urls import path

from hw.apps import HwConfig
from hw.views import index, contact

app_name = HwConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact')
]
