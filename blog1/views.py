from django.shortcuts import render

from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog1/homie.html', context=context)


def about(request):
    return render(request, 'blog1/about.html', context={'title': 'About'})

