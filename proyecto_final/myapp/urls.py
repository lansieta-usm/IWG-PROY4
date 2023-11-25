from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('users/', views.user, name="users"),
    path('anadir/', views.registro_usuario, name="anadir"),
    path('blog/', views.blog, name="blog"), 
    path('blog/post-1/', views.post1, name="post-1"),
    path('blog/post-2/', views.post2, name="post-2"),
    path('blog/post-3/', views.post3, name="post-3"),
    path('perfil/', views.perfil, name="perfil"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('signin/', views.signin, name="signin"),
]