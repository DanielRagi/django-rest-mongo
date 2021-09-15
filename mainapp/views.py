from django.shortcuts import render, redirect, HttpResponse
from rest_framework import viewsets

from .serializers import SerializeMovie
from .models import MovieDetails


# REST API CLASS
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieDetails.objects.all().order_by('name')
    serializer_class = SerializeMovie


def view(request):
    if request.method == 'GET':
        details = MovieDetails.objects.all()
        return render(request, 'mainapp/view.html', {"details": details})
    else:
        if request.POST['action'] == 'Actualizar':
            if(MovieDetails.objects.filter(name=request.POST['name']).update(
                genre=request.POST['genre'],
                description=request.POST['description'],
                director=request.POST['director'],
                year=request.POST['year']
            )):
                return HttpResponse("<script>alert('Actualización realizada.');location.href = '/'</script>")
            else:
                return HttpResponse("<script>alert('Algo salió mal.');location.href = '/'</script>")

        elif request.POST['action'] == 'Eliminar':
            if(MovieDetails.objects.filter(name=request.POST['name']).delete()[0]):
                return HttpResponse("<script>alert('Eliminado exitosamente');location.href = '/'</script>")
            else:
                return HttpResponse("<script>alert('Algo salió mal.');location.href = '/'</script>")


def add(request):
    if request.method == 'GET':
        return render(request, 'mainapp/add.html')
    else:
        s = MovieDetails(name=request.POST['name'],
                           genre=request.POST['genre'],
                           description=request.POST['description'],
                           director=request.POST['director'],
                           year=request.POST['year'])
        s.save()
        return HttpResponse("<script>alert('Petición exitosa.');location.href = '/'</script>")


