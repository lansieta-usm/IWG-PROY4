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

"""
def registro_usuario(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            print("yes")
            # Obtener los valores del formulario
            name = form.cleaned_data['name']
            alergias = form.cleaned_data['alergias']
            contact = form.cleaned_data['contact']
            num_contact = form.cleaned_data['num_contact']
            condicion = form.cleaned_data['condicion']

            # Buscar la condición médica correspondiente
            try:
                condicion_obj = Condicion.objects.get(condicion=condicion)
                recomendaciones_condicion = condicion_obj.recomendacion
            except Condicion.DoesNotExist:
                recomendaciones_condicion = "No se encontraron recomendaciones para esta condición."

            # Crear y guardar la instancia del modelo Usuario
            usuario = Usuario(
                name=name,
                alergias=alergias,
                contact=contact,
                num_contact=num_contact,
                padecimiento=condicion,  # Completar automáticamente
                recomendaciones_condicion=recomendaciones_condicion  # Completar automáticamente
            )
            usuario.save()

            return redirect(home)  # Redirigir a una página de éxito de registro
        else:
            print("xale")
            print(form.errors)

    else:
        form = RegistroUsuarioForm()

    return render(request, 'añadir.html', {'form': form})
"""
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Obtener los valores del formulario
            name = form.cleaned_data['name'].strip()
            alergias = form.cleaned_data['alergias'].strip()
            contact = form.cleaned_data['contact'].strip()
            num_contact = form.cleaned_data['num_contact']
            condicion = form.cleaned_data['condicion']

            # Buscar la condición médica correspondiente
            try:
                condicion_obj = Condicion.objects.get(condicion=condicion)
                print(condicion_obj)
                recomendaciones_condicion = condicion_obj.recomendacion
                print(recomendaciones_condicion)
            except Condicion.DoesNotExist:
                recomendaciones_condicion = "No se encontraron recomendaciones para esta condición."
                print("a")

            # Crear y guardar la instancia del modelo Usuario
            usuario = Usuario(
                name=name,
                alergias=alergias,
                contact=contact,
                num_contact=num_contact,
                padecimiento=condicion,  # Asigna directamente el objeto Condicion
                recomendaciones_condicion=recomendaciones_condicion
            )
            usuario.save()

            return redirect(home)  # Redirigir a una página de éxito de registro
        else:
            print("xale")

    else:
        form = RegistroUsuarioForm()

    return render(request, 'añadir.html', {'form': form})
