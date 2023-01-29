from django.urls import path
from . import views
from critica_cine.views import PeliculasListView, EstrenosListView, PeliculaDetailView, SeriesListView,SerieDetailView, EstrenoDetailView, PeliculasUpdateView, SeriesUpdateView, EstrenosUpdateView, PeliculasDeleteView, SeriesDeleteView, EstrenosDeleteView, registro, login_view, CustomLogoutView,ProfileUpdateView, agregar_avatar, listar_peliculas
from django.conf import Settings 

urlpatterns = [
    path("inicio", views.saludar, name="inicio"),
    #path("peliculas/", views.listar_peliculas, name="peliculas"),
    #path("series/", views.listar_series, name="series"),
    #path("estrenos/", views.listar_estrenos, name="estrenos"),
    path("about/", views.about, name="about"),
    path("crear-serie/", views.crear_serie, name="crear_serie"),
    path("crear-pelicula/", views.crear_pelicula, name="crear_pelicula"),
    path("crear-estreno/", views.crear_estreno, name="crear_estreno"),
    path("buscar-pelicula/", views.buscar_pelicula, name="buscar_pelicula"),
    # creado con class list
    path("peliculas/" ,views.listar_peliculas ,name="peliculas"),
    path("series/",SeriesListView.as_view(), name="series"),
    path("estrenos/",EstrenosListView.as_view(), name="estrenos"),
    path("ver-pelicula/<int:pk>/",PeliculaDetailView.as_view(), name="ver_pelicula"),
    path("ver-serie/<int:pk>/",SerieDetailView.as_view(), name="ver_serie"),
    path("ver-estreno/<int:pk>/", EstrenoDetailView.as_view(), name="ver_estreno"),
    path("editar-pelicula/<int:pk>/",PeliculasUpdateView.as_view (), name="editar_pelicula"),
    path("editar-serie/<int:pk>/",SeriesUpdateView.as_view (), name="editar_serie"),
    path("editar-estreno/<int:pk>/",EstrenosUpdateView.as_view (), name="editar_estreno"),
    path("eliminar-pelicula/<int:pk>/",PeliculasDeleteView.as_view (), name="eliminar_pelicula"),
    path("eliminar-serie/<int:pk>/",SeriesDeleteView.as_view (), name="eliminar_serie"),
    path("eliminar-estreno/<int:pk>/",EstrenosDeleteView.as_view (), name="eliminar_estreno"),
    path("registro/",registro, name="registro"),
    path("login/",login_view, name="login"),
    path("logout/",CustomLogoutView.as_view(), name="logout"),
    #url perfil
    path("editar-perfil/",ProfileUpdateView.as_view(), name="editar_perfil"),
    path("agregar-avatar/",views.agregar_avatar, name="agregar_avatar"),


]