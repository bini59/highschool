from django.shortcuts import render, redirect
from .models import Post

from django.utils import timezone

def convertTime(target_time):
    # 현재 시간
    now = timezone.now()
    
    # 대상 시간과 현재 시간 간의 차이 계산
    delta = now - target_time
    
    # delta에서 초, 분, 시간, 일, 달, 년을 추출
    seconds = delta.total_seconds()
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    months = days / 30
    years = days / 365
    
    if years >= 1:
        return f"{int(years)}년 전"
    elif months >= 1:
        return f"{int(months)}개월 전"
    elif days >= 1:
        return f"{int(days)}일 전"
    elif hours >= 1:
        return f"{int(hours)}시간 전"
    elif minutes >= 1:
        return f"{int(minutes)}분 전"
    else:
        return f"{int(seconds)}초 전"

# Create your views here.
def index(request):
    postList = Post.objects.order_by('-created_at')
    for post in postList:
        post.created_at = convertTime(post.created_at)
    context = {'postList': postList}
    return render(request, 'lily/index.html', context)


def post_POST(request):
    post = Post()
    try:
        if request.POST['title'] == "" or request.POST['content'] == "":
            raise Exception()
        
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.author = request.user
        post.created_at = timezone.datetime.now()
        if request.FILES.get('image') is not None:
            post.image = request.FILES['image']
        post.save()
        
        return redirect('/')
    except:
        return render(request, 'lily/post.html', {'form': request.POST})
    
    
    

def post_GET(request):
    return render(request, 'lily/post.html')

def post(request):
    if request.method == 'POST':
        return post_POST(request)
    elif request.method == 'GET':
        return post_GET(request)
        