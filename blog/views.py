from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import BlogEntry


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ('title', 'body', 'is_published', 'preview')
    success_url = reverse_lazy('blog:list_view')


class BlogEntryListView(ListView):
    model = BlogEntry

    def get_context_data(self, *args, **kwargs):
        context = super(BlogEntryListView, self).get_context_data(**kwargs)
        context['title'] = 'Список записей'
        return context


class BlogEntryDetailView(DetailView):
    model = BlogEntry


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ('title', 'body', 'is_published', 'preview')
    success_url = reverse_lazy('blog:list_view')


class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:list_view')

