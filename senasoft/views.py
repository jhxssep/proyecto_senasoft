from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Competidor

def bienvenida(request):
    """
    Responde a: http://127.0.0.1:8000/senasoft/
    Muestra el mensaje de bienvenida al evento.
    """
    return render(request, "senasoft/bienvenida.html")

def registro(request):
    """
    Responde a: http://127.0.0.1:8000/senasoft/registro/
    GET: Carga el formulario solicitando nombre, centro y categoría.
    POST: Almacena los datos en la base de datos y redirige al listado.
    """
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        centro = request.POST.get("centro")
        categoria = request.POST.get("categoria")

        if not (nombre and centro and categoria):
            return HttpResponse(
                "Todos los campos (nombre, centro y categoría) son obligatorios.",
                status=400
            )

        Competidor.objects.create(
            nombre=nombre,
            centro=centro,
            categoria=categoria
        )

        return redirect("competidores")

    return render(request, "senasoft/registro.html")

def competidores(request):
    """
    Responde a: http://127.0.0.1:8000/senasoft/competidores/
    Muestra la información de todos los competidores inscritos.
    """
    lista_competidores = Competidor.objects.all().order_by("-fecha_registro")
    return render(request, "senasoft/competidores.html", {"competidores": lista_competidores})
