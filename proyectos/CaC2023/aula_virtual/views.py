from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def inicio(request):
    return HttpResponse("Bienvenidos al aula virtual 2.0")

def saludar(request, nombre):
    return HttpResponse(f"<h2>Hola , {nombre.upper()} Bienvenido al aula virtula")

def alta_alumno(request):
    return HttpResponse("Alta de alumnos nuevos")

def baja_alumno(request):
    return HttpResponse("Baja de alumnos en acticidad")

def alumnos_2023(request):
    return HttpResponse(
        "<h2>Listado de alumnos 2023</h2>"+
        "<p>1 - Carlos Lopez</p>"+
        "<p>2 - Maria Del Cerro</p>"+
        "<p>3 - Jose Perez</p>"
    )
    
def alumnos_by_year(request, year):
    if int(year) < 2020:
        return HttpResponseNotFound("<h2>No hay registros para ese año </h2>")
    else:
        return HttpResponse(
        f"<h2>Listado de alumnos {year}</h2>"+
        "<p>2023: 50 alumnos</p>"+
        "<p>2022: 35 alumnos inscriptos</p>"+
        "<p>2021: 127 alumnos inscriptos</p>"
        )
        
def alumnos_by_year_month(request, year, month):
    if int(year) < 2020:
        return HttpResponseNotFound("<h2>No hay registros para ese año </h2>")
    else:
        if int(month) > 4:
            return HttpResponseNotFound("<h2>Solo hay registros para el primer cuatrimestre del año </h2>")
        else:
            return HttpResponse(
            f"<h2>Listado de alumnos {year}</h2>"+
            "<p>2023: 50 alumnos</p>"+
            "<p>2022: 35 alumnos inscriptos</p>"+
            "<p>2021: 127 alumnos inscriptos</p>"
        ) 

def docentes_by_year(request, year, curso):
    return HttpResponse(
        f"<h2>Docentes correspondientes al año: {year} del curso de {curso}</h2>"+
        "<p>Decente 1</p>"+
        "<p>Decente 1</p>"
        )    

    