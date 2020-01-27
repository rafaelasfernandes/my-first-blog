from django.shortcuts import render
from .models import Post
from django.utils import timezone

def lista_post(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/lista_post.html', {'posts' : posts})
