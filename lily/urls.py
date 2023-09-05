from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from lily import views

urlpatterns = [
    path('post/', views.post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
