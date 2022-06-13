from django.urls import path
from blog_app import views

urlpatterns =[
    path('', views.PostList.as_view(), name='post_list'), #path to main page (post list)
    path('post/<int:pk>/', views.PostDetail.as_view(),name='post_detail'), #path to selected post
    path('post/create/', views.CreatePost.as_view(),name='post_new'), #path to create new post
    path('post/<int:pk>/create/', views.post_create,name='post_create'), #new post creation func.
    path('post/<int:pk>/like/', views.post_like, name='post_like'), #post like func.
]


