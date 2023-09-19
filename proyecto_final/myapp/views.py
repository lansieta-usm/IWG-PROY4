from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from .models import Usuario, Condicion

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
        Usuario.objects.create(
            name = request.POST['name'].strip(),
            alergias = request.POST['alergias'].strip(),
            contact = request.POST['contact'].strip(),
            num_contact = request.POST['num_contact'],
            padecimiento = request.POST['condicion'],
            recomendaciones_condicion = Condicion.objects.get(condicion=condicion_b[0]).recomendacion
        )
        return redirect(home)
        
    else:
        form = RegistroUsuarioForm()
        return render(request, 'añadir.html', {'form': form})
