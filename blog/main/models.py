from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class News(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)
    text = models.TextField('Содержание статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    views = models.IntegerField('Просмотры', default=1)
    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    # )
    # shop_sizes = models.CharField(max_length=1, choices=sizes, default='S')

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title