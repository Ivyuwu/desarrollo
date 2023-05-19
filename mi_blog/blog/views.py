from django.shortcuts import render
from django.contrib import messages
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    if request.method == 'POST':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post_form.save()
                messages.success(request, 'La publicación ha sido guardada exitosamente')
            else:
                 messages.error(request, 'Ha ocurrido un error al guardar la publicación')
    post_form = PostForm()
    return render(request, 'blog/post_list.html', {'posts':posts, 'formulario': post_form})

