from django.shortcuts import render, redirect
from .models import Cliente,Mascotas
from .forms import ClienteForm,MascotaForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'quienes somos.html')

def galeria(request):
    return render(request, 'galeria.html')

def pokedex(request):
    return render(request, 'pokeapi.html')

def formulario(request):
    return render(request, 'form.html')

def clientes(request):
    cliente = Cliente.objects.all()
    datos={
        'clien':cliente
    }
    return render(request, 'clientes.html', datos)

def eliminar(request, id):
    cliente = Cliente.objects.get(rutcliente=id)
    cliente.delete()
    return redirect('clientes')

def crear(request):
    if request.method=='POST': 
        Clienteform = ClienteForm(request.POST)
        if Clienteform.is_valid():
            Clienteform.save()     
            return redirect('clientes')
    else:
        Clienteform=ClienteForm()
    return render(request, 'ingresarclientes.html', {'Clienteform': Clienteform})

def modificar(request, id):
    cliente = Cliente.objects.get(rutcliente=id) 
    datos ={
        'form': ClienteForm(instance=cliente) 
    }
    if request.method=='POST':
        formulario1 = ClienteForm(data=request.POST, instance=cliente)
        if formulario1.is_valid:
            formulario1.save()
            return redirect('clientes')
    
    return render(request, 'modificar.html', datos)

def mascotas(request):
    mascota = Mascotas.objects.all()
    datos={
        'cota':mascota
    }
    return render(request, 'mascotas.html', datos)

def eliminacota(request, id1):
    mascota = Mascotas.objects.get(codmascota=id1)
    mascota.delete()
    return redirect('mascotas')

def crearcota(request):
    if request.method=='POST': 
        mascotaform = MascotaForm(request.POST, request.FILES)
        if mascotaform.is_valid():
            mascotaform.save()     
            return redirect('mascotas')
    else:
        mascotaform=MascotaForm()
    return render(request, 'ingresarmascota.html', {'mascotaform': mascotaform})

def modificacota(request, id1):
    mascota = Mascotas.objects.get(codmascota=id1) 
    datos ={
        'form': MascotaForm(instance=mascota) 
    }
    if request.method=='POST':
        formulario2 = MascotaForm(data=request.POST, instance=mascota)
        if formulario2.is_valid:
            formulario2.save()
            return redirect('mascotas')
    
    return render(request, 'modificarcota.html', datos)

