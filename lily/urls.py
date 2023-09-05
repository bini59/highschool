from django.urls import path


from lily import views

urlpatterns = [
    path('post/', views.post, name='post'),
]
