from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList, name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/',views.PostCreateView.as_view(), name = 'post-create'),
]