from django.urls import path

from hw.apps import HwConfig
from hw.views import index

app_name = HwConfig.name

urlpatterns = [
    path('', index, name='index')
]
