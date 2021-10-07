from django.shortcuts import render, get_object_or_404
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.


class ShowNewsView(ListView):
    model = News
    template_name = 'main/index.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 2

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'main/news_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class DeleteNewsView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    model = News
    success_url = '/'
    template_name = 'main/delete_news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'main/create_news.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'main/create_news.html'

    fields = ['title', 'text']

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx


def contacti(request):

    return render(request, 'main/contacti.html', {'title': 'Страница контакты!'})


class UserAllNewsView(ListView):
    model = News
    template_name = 'main/user_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)
        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
        return ctx