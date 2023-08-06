from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from fresh_basket.blog.forms import PostForm
from fresh_basket.blog.models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'blogs/post-list.html'
    context_object_name = 'posts'
    form_class = PostForm


class PostDetailsView(DetailView):
    model = Post
    template_name = 'blogs/post-details.html'
    context_object_name = 'post'


class PostAddPageView(TemplateView):
    model = Post
    template_name = 'blogs/post-add.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/post-add.html'
    success_url = reverse_lazy('posts-all')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
