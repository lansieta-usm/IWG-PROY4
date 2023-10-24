#
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroUsuarioForm
from .models import Usuario, Condicion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def user(request):
    users = Usuario.objects.all()
    return render(request, "users.html", {"users" : users})

def añadir(request):
    return render(request, "añadir.html")

def blog(request):
    return render(request, "blog.html")

def registro_usuario(request):
    if request.method == 'POST':
        condicion_b = request.POST['condicion'],
        condicion_b = list(condicion_b)
        #print(condicion_b[0])
        new_user = Usuario.objects.create(
            name = request.POST['name'].strip(),
            alergias = request.POST['alergias'].strip(),
            contact = request.POST['contact'].strip(),
            num_contact = request.POST['num_contact'],
            padecimiento = request.POST['condicion'],
            recomendaciones_condicion = Condicion.objects.get(condicion=condicion_b[0]).recomendacion,
            user=request.user
        )
        #new_user_id = new_user.id

        return redirect(perfil)
        
    else:
        form = RegistroUsuarioForm()
        return render(request, 'añadir.html', {'form': form})

@login_required
def perfil(request):
    u = Usuario.objects.get(user=request.user)
    return render(request, "perfil.html", {"perfil": u})

def signup(request):
    if request.method == "GET":
            return render(request, "signup.html", {
        "form": UserCreationForm
    })

    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user= User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("anadir")
            except IntegrityError:
                return render(request, "signup.html", {
        "form": UserCreationForm,  "error": "Usuario ya existe"
    })
        return render(request, "signup.html", {
        "form": UserCreationForm,  "error": "Contraseñas no coinciden"
        })
    
def signout(request):
    logout(request)
    return redirect("home")

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
        "form": AuthenticationForm
    })
    else:
        user= authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "signin.html", {
        "form": AuthenticationForm, "error": "Usuario o contraseña incorrecta"
    })
        else:
            login(request, user)
            return redirect("perfil")
