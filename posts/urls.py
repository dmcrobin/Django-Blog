from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    # path('add/', views.index, name='add_post'),
    path('del/<slug:slug>/', views.delPost, name="del_post"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail")
]