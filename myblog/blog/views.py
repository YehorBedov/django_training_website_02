from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm


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


class AddComments(View):
    '''Добовление комментариев'''
    def post(self, request, pk):
        # print(request.POST)
        # return redirect('/')
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save() # после присвоения id сново сохраняем данные
        return redirect(f'/{pk}')