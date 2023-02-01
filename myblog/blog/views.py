from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
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


def get_client_ip(request):
    '''Получение IP пользователя (для учета лайков)'''
    x_forwarded_for = request.META.get('HTTP_X_ FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0] # из списка получаем первое значение (ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    '''счетчик лайков'''
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class DelLike(View):
    '''счетчик дизлайков'''
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client, pos_id=pk)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')


