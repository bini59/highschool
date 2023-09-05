from django.shortcuts import render, redirect
from .models import Post

from django.utils import timezone

# Create your views here.
def index(request):
    postList = Post.objects.order_by('-created_at')
    context = {'postList': postList}
    return render(request, 'lily/index.html', context)


def post_POST(request):
    post = Post()
    print(request.FILES['image'])
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.author = request.user
    post.created_at = timezone.datetime.now()
    post.image = request.FILES['image']
    post.save()
    
    return redirect('/')

def post_GET(request):
    return render(request, 'lily/post.html')

def post(request):
    if request.method == 'POST':
        return post_POST(request)
    elif request.method == 'GET':
        return post_GET(request)
        