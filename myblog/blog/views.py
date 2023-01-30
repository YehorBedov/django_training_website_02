from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


# Create your views here.
class PostView(View):
    '''вывод записей из базы (models)'''

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDitail(View):
    '''отдельная страница записей для комментарий'''

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_ditail.html', {'post': post})