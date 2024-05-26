from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, BlogPost


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.first(is_published=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'photo', 'created_at', 'is_published')
    success_url = reverse_lazy('blogpost:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'photo', 'created_at', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogpost:view', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost:list')

