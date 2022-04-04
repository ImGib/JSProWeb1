from urllib import request
from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'home_views.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.blog_views += 1
        obj.save()
        return obj

def PostList(request):
    post_list = Post.objects.filter(Post.is_published==True).order_by('-created_on')
    return render(request, 'index.html', {'post_list':post_list})

class PostCreateView(LoginRequiredMixin,generic.CreateView):
    model = Post
    fields = ['title', 'content', 'status']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)