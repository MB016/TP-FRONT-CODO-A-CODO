from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Libro
import json

# Create your views here.


class LibroView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            libros = list(Libro.objects.filter(id=id).values())
            if len(libros) > 0:
                libro = libros[0]
                datos = {'message': "Éxito", 'libro': libro}
            else:
                datos = {'message': "Libro no encontrado..."}
            return JsonResponse(datos)
        else:
            libros = list(Libro.objects.values())
            if len(libros) > 0:
                datos = {'message': "Éxito", 'libros': libros}
            else:
                datos = {'message': "Libros no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Libro.objects.create(titulo=jd['titulo'], autor=jd['autor'], editorial=jd['editorial'],genero=jd['genero'],año_publicacion=jd['año_publicacion'])
        datos = {'message': "Éxito"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        libros = list(Libro.objects.filter(id=id).values())
        if len(libros) > 0:
            libro = Libro.objects.get(id=id)
            libro.titulo = jd['titulo']
            libro.autor = jd['autor']
            libro.editorial = jd['editorial']
            libro.genero = jd['genero']
            libro.año_publicacion = jd['año_publicacion']
            libro.save()
            datos = {'message': "Éxito"}
        else:
            datos = {'message': "Libro no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        libros = list(Libro.objects.filter(id=id).values())
        if len(libros) > 0:
            Libro.objects.filter(id=id).delete()
            datos = {'message': "Éxito"}
        else:
            datos = {'message': "Libro no encontrado..."}
        return JsonResponse(datos)