from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # formを保存。authorを追加
            post = form.save(commit=False) # まだPostモデルを保存しない
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # 新しく作ったポストのdetailページに移動
            # post_detailは移動したいビューの名前。このビューはpk変数は必須。postは新しくつくられたブログポスト
            return redirect('post_detail', pk=post.pk)
        
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})


