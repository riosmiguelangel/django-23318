#from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    #return render(request, "index.html")
    return render(request, "index.html", {"hoy": datetime.now })

def articulo(request):
    return render(request, "articulo.html")
    