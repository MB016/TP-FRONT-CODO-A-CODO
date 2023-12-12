"""
URL configuration for cac_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path ,include
from .views import LandingPage
from .views import RegistroPage
from .views import LoginPage
from .views import ComicPage1
from .views import ComicPage2
from .views import ComicPage3
from .views import ComicPage4
from .views import ComicPage5
from .views import ComicPage6
from .views import LibroPage1
from .views import LibroPage2
from .views import LibroPage3
from .views import LibroPage4
from .views import LibroPage5
from .views import LibroPage6
from .views import LibroPage7
from .views import LibroPage8
from .views import LibroPage9
from .views import LibroPage10
from .views import ModoCreador
from .views import index1



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",LandingPage.as_view(),name="index"),
    path("ModoCreador/",ModoCreador.as_view(),name="ModoCreador"),
    path("Registro/",RegistroPage.as_view(),name="Registro"),
    path("Login/",LoginPage.as_view(),name="Login"),
    path("Libro/",LibroPage1.as_view(),name="Libro1"),
    path("Libro2/",LibroPage2.as_view(),name="Libro2"),
    path("Libro3/",LibroPage3.as_view(),name="Libro3"),
    path("Libro4/",LibroPage4.as_view(),name="Libro4"),
    path("Libro5/",LibroPage5.as_view(),name="Libro5"),
    path("Libro6/",LibroPage6.as_view(),name="Libro6"),
    path("Libro7/",LibroPage7.as_view(),name="Libro7"),
    path("Libro8/",LibroPage8.as_view(),name="Libro8"),
    path("Libro9/",LibroPage9.as_view(),name="Libro9"),
    path("Libro10/",LibroPage10.as_view(),name="Libro10"),
    path("Comic1/",ComicPage1.as_view(),name="Comic1"),
    path("Comic2/",ComicPage2.as_view(),name="Comic2"),
    path("Comic3/",ComicPage3.as_view(),name="Comic3"),
    path("Comic4/",ComicPage4.as_view(),name="Comic4"),
    path("Comic5/",ComicPage5.as_view(),name="Comic5"),
    path("Comic6/",ComicPage6.as_view(),name="Comic6"),
    path("index1/",index1.as_view(),name="index1"),
    path("Creador/",include("creador_app.urls"))
]
