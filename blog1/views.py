from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog1/homie.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog1/homie.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog1/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog1/about.html', context={'title': 'About'})

