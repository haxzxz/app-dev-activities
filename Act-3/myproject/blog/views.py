from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

def home(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    return redirect('login')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post)
    
    context = {
        'post' : post,
        'comments' : comments
    }
    
    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_form.html', {'form': form})

def comment_add(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, 'blog/comment_form.html', {'form': form})
                
# Authentication Views
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_list')
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', pk=post.pk)
    
    return render(request, 'blog/post_form.html', {'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_list')
    
    post.delete()
    return redirect('post_list')

    