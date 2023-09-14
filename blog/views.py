from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogEntry


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ('title', 'body', 'is_published', 'preview')
    success_url = reverse_lazy('blog:list_view')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogEntryListView(ListView):
    model = BlogEntry

    def get_context_data(self, *args, **kwargs):
        context = super(BlogEntryListView, self).get_context_data(**kwargs)
        context['title'] = 'Список записей'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogEntryDetailView(DetailView):
    model = BlogEntry

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()

        return self.object


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ('title', 'body', 'is_published', 'preview')

    def form_valid(self, form, *args, **kwargs):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail_view', args=[self.kwargs.get('pk')])


class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:list_view')
