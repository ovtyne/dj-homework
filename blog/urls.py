from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogEntryCreateView, BlogEntryDetailView, BlogEntryListView, BlogEntryUpdateView, \
    BlogEntryDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogEntryCreateView.as_view(), name='create'),
    path('detail_view/<int:pk>', BlogEntryDetailView.as_view(), name='detail_view'),
    path('', BlogEntryListView.as_view(), name='list_view'),
    path('edit/<int:pk>', BlogEntryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BlogEntryDeleteView.as_view(), name='delete'),
]
