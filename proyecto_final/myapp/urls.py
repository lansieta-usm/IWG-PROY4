from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),  #No priotidad 1
    path('users/', views.user, name="users"),
    path('anadir/', views.registro_usuario, name="anadir"),
    path('blog/', views.blog, name="blog"),  #no prioridad 2
    path('perfil/<int:id>', views.perfil, name="perfil"),
]