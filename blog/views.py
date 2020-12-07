from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Product1
from .models import Product2
from .models import Product3
from .models import Product4
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import ListView

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

def products1(request):
    products = Product1.objects.all()
    return render(request, 'blog/products1.html', {'posts': products})

def products2(request):
    products = Product2.objects.all()
    return render(request, 'blog/products2.html', {'posts': products})

def products3(request):
    products = Product3.objects.all()
    return render(request, 'blog/products3.html', {'posts': products})

def products4(request):
    products = Product4.objects.all()
    return render(request, 'blog/products4.html', {'posts': products})