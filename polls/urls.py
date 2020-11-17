from django.urls import path

from . import views

urlpatterns = [
    # path 四个参数，分别是 route、view、kwargs 和 name
    # - name 在 Django 中任何位置都能是指
    path('', views.index, name='index2')  # '' 路由到 index 方法
]
