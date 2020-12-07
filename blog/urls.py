from django.urls import path
from django.conf.urls import url
from . import views

from .views import HomePageView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('', HomePageView.as_view(), name='home'),
    url(r'^products1/$', views.products1, name='products1'),
    url(r'^products2/$', views.products2, name='products2'),
    url(r'^products3/$', views.products3, name='products3'),
    url(r'^products4/$', views.products4, name='products4'),
]