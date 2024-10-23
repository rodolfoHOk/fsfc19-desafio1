from django.shortcuts import render
from django.template import loader
from core.models import Post, Tag

# Create your views here.
def blog(request):
  posts = Post.objects.all().values()
  tags = Tag.objects.all().values()
  context = {
    'posts': posts,
    'tags': tags 
  }
  return render(request, 'blog/blog.html', context=context)
