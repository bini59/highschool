from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    postList = Post.objects.order_by('-created_at')
    context = {'postList': postList}
    return render(request, 'lily/index.html', context)