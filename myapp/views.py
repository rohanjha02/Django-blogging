from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from bson import ObjectId
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import EditPostForm  # Make sure to import the correct form
from bson import ObjectId


def post_list(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.get_id)  # Check what IDs are being outputted
    return render(request, 'myapp/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'myapp/add_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, _id=ObjectId(pk))
    return render(request, 'myapp/post_detail.html', {'post': post})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import EditPostForm  # Import the correct form
from bson import ObjectId

def edit_post(request, pk):
    post = get_object_or_404(Post, _id=ObjectId(pk))
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)  # Use the EditPostForm that excludes the image
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.get_id)
    else:
        form = EditPostForm(instance=post)  # Also use EditPostForm here

    return render(request, 'myapp/edit_post.html', {'form': form, 'post': post})




from django.shortcuts import redirect

def delete_post(request, pk):
    post = get_object_or_404(Post, _id=ObjectId(pk))
    post.delete()
    return redirect('post_list')  # Redirect to the list of posts



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from bson import ObjectId

@csrf_exempt  # Use this decorator cautiously
def like_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, _id=ObjectId(pk))
        post.likes += 1
        post.save()
        return JsonResponse({'likes': post.likes})
    else:
        return JsonResponse({'error': 'This action must be done via POST.'}, status=400)


