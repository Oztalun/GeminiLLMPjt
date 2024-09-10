from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.products, name="products"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("index/", views.index, name="index"),
    path("<int:pk>/update/", views.update, name="update"),
    # path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    # path("<int:pk>/comments_delete/", views.comment_delete, name="comment_delete"),
    path("<int:pk>/like/", views.like, name="like"),
    path("hello/", views.hello, name="hello"),# 지우랬는데 안지울거임
    path("data_throw/", views.data_throw, name="data-throw"),
    path("data_catch/", views.data_catch, name="data-catch"),
]