from django.db import models


# Create your models here.
class Post(models.Model):
    '''база записей'''
    title = models.CharField('Заголовок записи', max_length=200)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=200)
    date = models.DateTimeField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    '''база комментариев'''
    email = models.EmailField()
    name = models.CharField('Имя пользователя', max_length=40)
    text_comments = models.TextField('Ваш комментарий', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE) # связывает таблицы с постами и комментариями

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    '''Счетчик лайков (по ip)'''
    ip = models.CharField('IP-адрес', max_length=50)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)



