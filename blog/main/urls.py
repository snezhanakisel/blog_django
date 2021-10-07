from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowNewsView.as_view(), name='index'),
    path('user/<str:username>', UserAllNewsView.as_view(), name='user-news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', DeleteNewsView.as_view(), name='news-delete'),
    path('news/add', CreateNewsView.as_view(), name='news-add'),
    path('contacti', contacti, name='contacti')
]