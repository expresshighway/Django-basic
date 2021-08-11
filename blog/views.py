from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(request):
  qs = Post.objects.all()
  qs = qs.filter(published_date__lte=timezone.now())
  qs = qs.order_by('published_date')

  return render(request, 'blog/post_list.html',{
    'post_list': qs,
  })

def post_detail(request, pk):
  # try:
  #   post = Post.objects.get(pk=pk)
  # except Post.DoesNotExist:
  #   raise Http404
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {
    'post': post
  })