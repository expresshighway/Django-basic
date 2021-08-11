from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
  qs = Post.objects.all()
  qs = qs.filter(published_date__lte=timezone.now())
  qs = qs.order_by('published_date')
  
  return render(request, 'blog/post_list.html',{
    'post_list': qs,
  })