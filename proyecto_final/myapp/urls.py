from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),  #No priotidad 1
    path('users/', views.user, name="users"),
    path('anadir/', views.registro_usuario, name="anadir"),
    path('blog/', views.blog, name="blog"),  #no prioridad 2
    path('perfil/', views.perfil, name="perfil"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('signin/', views.signin, name="signin"),
]