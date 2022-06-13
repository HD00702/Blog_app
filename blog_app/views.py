from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from blog_app.models import Post
from blog_app.forms import PostForm
from django.utils import timezone

# Create your views here.

class PostList(ListView):
    model = Post


    def get_queryset(self): #query on my model
        return Post.objects.filter(date_created__lte=timezone.now()).order_by('-date_created') #order by date created(reverse)

class PostDetail(DetailView):
    model = Post

class CreatePost(CreateView):
    model = Post
    redirect_field_name ='blog_app/post_form.html'
    form_class = PostForm


def post_create(request): #creating new post
    post= Post()
    post.create()
    return redirect('post_detail')

def post_like(request, pk):  #like/unlike post
    post =Post.objects.get(pk=pk)
    if post.is_liked == False:
        post.is_liked = True
    else:
        post.is_liked = False
    post.save()

    return redirect('post_list')
