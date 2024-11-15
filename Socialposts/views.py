from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from PIL import Image
import io
# Create your views here.


def home(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'socialpost/home.html', context)


@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            uploaded_image = form.cleaned_data['image']

            # Check if the image size exceeds 3MB (3 * 1024 * 1024 bytes)
            if uploaded_image.size > 3 * 1024 * 1024:

                # Compress the image
                img = Image.open(uploaded_image)
                output_format = img.format
                buffer = io.BytesIO()

                # Compress the image with reduced quality
                img.save(buffer, format=output_format, quality=60)
                buffer.seek(0)

                # Save the compressed image to the Post model
                post.image.save(f'compressed_{uploaded_image.name}', buffer)
                post.save()
                form.save_m2m()

                # Provide a download option for the compressed image
                response = HttpResponse(
                    buffer.getvalue(), content_type=f'image/{output_format.lower()}'
                )
                response['Content-Disposition'] = f'attachment; filename=compressed_{uploaded_image.name}'

                response.write(
                    '<html><head><meta http-equiv="refresh" content="1;url=/home/"></head></html>'
                )

                # Automatically triggers download of the compressed image
                return response

            else:
                # If image size is <= 3MB, save directly
                post.image = uploaded_image
                post.save()
                form.save_m2m()
                return redirect('home')
    else:
        form = PostCreateForm()

    return render(request, 'socialpost/post_create.html', {'form': form})
# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostCreateForm(request.POST, request.FILES)

#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             uploaded_image = form.cleaned_data['image']

#             # Check if the image size exceeds 3MB (3 * 1024 * 1024 bytes)
#             if uploaded_image.size > 3 * 1024 * 1024:

#                 # Compress the image
#                 img = Image.open(uploaded_image)
#                 output_format = img.format
#                 buffer = io.BytesIO()

#                 # Compress the image with reduced quality
#                 img.save(buffer, format=output_format, quality=60)
#                 buffer.seek(0)

#                 # Save the compressed image to the Post model
#                 post.image.save(f'compressed_{uploaded_image.name}', buffer)

#                 # Provide a download option for the compressed image
#                 response = HttpResponse(
#                     buffer.getvalue(), content_type=f'image/{output_format.lower()}'
#                 )
#                 response['Content-Disposition'] = f'attachment; filename=compressed_{uploaded_image.name}'
#                 # Automatically triggers download of the compressed image
#                 return redirect('home')

#             else:
#                 # If image size is <= 3MB, save directly
#                 post.image = uploaded_image
#                 post.save()
#                 form.save_m2m()
#                 return redirect('home')
#     else:
#         form = PostCreateForm()

#     return render(request, 'socialpost/post_create.html', {'form': form})


@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted')
        return redirect('home')

    return render(request, 'socialpost/post_delete.html', {'post': post})


@login_required
def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            messages.success(request, 'Post Updated')
            return redirect('home')
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'socialpost/post_edit.html', context)


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    commentform = CommentCreateForm()
    replyform = ReplyCreateForm()

    context = {
        'post': post,
        'commentform': commentform,
        'replyform': replyform,
    }

    return render(request, 'socialpost/post_page.html', context)


@login_required
def comment_sent(request, pk):
    post = get_object_or_404(Post, id=pk)
    replyform = ReplyCreateForm()

    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()

    context = {
        'post': post,
        'comment': comment,
        'replyform': replyform
    }
    return redirect('post', post.id)


@login_required
def comment_delete_view(request, pk):
    post = get_object_or_404(Comment, id=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Comment deleted')
        return redirect('post', post.parent_post.id)

    return render(request, 'socialpost/comment_delete.html', {'comment': post})


@login_required
def reply_sent(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    # replyform = ReplyCreateForm()

    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment
            reply.save()

    return redirect('post', comment.parent_post.id)


@login_required
def reply_delete_view(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)

    if request.method == "POST":
        reply.delete()
        messages.success(request, 'Reply deleted')
        return redirect('post', reply.parent_comment.parent_post.id)

    return render(request, 'socialpost/reply_delete.html', {'reply': reply})


def like_toggle(model):
    def inner_func(func):
        def wrapper(request, *args, **kwargs):
            post = get_object_or_404(model, id=kwargs.get('pk'))
            user_exist = post.likes.filter(
                username=request.user.username).exists()

            if post.author != request.user:
                if user_exist:
                    post.likes.remove(request.user)
                else:
                    post.likes.add(request.user)

            return func(request, post)
        return wrapper
    return inner_func


@login_required
@like_toggle(Post)
def like_post(request, post):
    return render(request, 'snippets/likes.html', {'post': post})


@login_required
@like_toggle(Comment)
def like_comment(request, post):
    return render(request, 'snippets/likes_comment.html', {'comment': post})


@login_required
@like_toggle(Reply)
def like_reply(request, post):
    return render(request, 'snippets/likes_reply.html', {'reply': post})
