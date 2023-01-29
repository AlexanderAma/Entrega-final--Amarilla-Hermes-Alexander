from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from critica_cine.forms import Peliculaformulario, Serieformulario, Estrenosformulario, UserRegisterForm, UserUpdateForm, AvatarFormulario
from critica_cine.models import Peliculas, Series, Proximos_estrenos, Avatar
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

 

# Create your views here.
def saludar(request):
     return render(
        request=request,
        template_name="critica_cine/saludar.html"
        )
    



def about(request):
    contexto= {"about": about}
    return render(
        request=request,
        template_name="critica_cine/about.html"
    )


def listar_peliculas(request):
    contexto = {
        "peliculas": Peliculas.objects.all()
    }
    return render(
        request=request, 
        template_name="critica_cine/lista_peliculas.html",
        context=contexto
        )


#def listar_series(request):
    contexto = {
        "series":Series.objects.all()
    }
    return render(
        request=request,
         template_name="critica_cine/lista_series.html",
         context=contexto
         )



#def listar_estrenos(request):
    contexto = {
        "estrenos":Proximos_estrenos.objects.all()
    }
    return render(
        request=request,
         template_name="critica_cine/lista_estrenos.html",
         context=contexto
         )

@login_required
def crear_serie(request):
    if request.method == "POST":
        formulario = Serieformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            serie = Series(nombre_de_pelicula=data["nombre_de_pelicula"], descripcion=data["descripcion"], director=data["director"], pais_de_origen=data["pais_de_origen"], plataforma=data["plataforma"] )
            serie.save()
            url_exitosa = reverse("series")
            return redirect(url_exitosa)

    else:

        formulario = Serieformulario()
    return render(
            request=request,
            template_name="critica_cine/formulario_serie.html",
            context= {"formulario": formulario},

        )
@login_required   
def crear_pelicula(request):
    if request.method == "POST":
       formulario = Peliculaformulario(request.POST)
       if formulario.is_valid():
        data = formulario.cleaned_data
        pelicula = Peliculas(nombre_de_pelicula=data["nombre_de_pelicula"], descripcion=data["descripcion"], director=data["director"], pais_de_origen=data["pais_de_origen"], fecha_estreno=data["fecha_estreno"] )
        pelicula.save()
        url_exitosa = reverse("peliculas")
        return redirect(url_exitosa)

    else:
        formulario =Peliculaformulario()
          
    return render(
            request=request,
            template_name="critica_cine/formulario_pelicula.html",
            context= {"formulario": formulario},
        )


@login_required
def crear_estreno(request):
    if request.method == "POST":
       formulario = Estrenosformulario(request.POST)
       if formulario.is_valid():
        data = formulario.cleaned_data
        estreno = Proximos_estrenos(nombre_de_pelicula=data["nombre_de_pelicula"], descripcion=data["descripcion"], director=data["director"], pais_de_origen=data["pais_de_origen"] )
        estreno.save()
        url_exitosa = reverse("estrenos")
        return redirect(url_exitosa)

    else:
        formulario =Estrenosformulario()
          
    return render(
            request=request,
            template_name="critica_cine/formulario_estreno.html",
            context= {"formulario": formulario},
        )

def buscar_pelicula(request):
    if request.method == "POST":
       data = request.POST
       peliculas = Peliculas.objects.filter(nombre_de_pelicula__contains= data["nombre_de_pelicula"])
       contexto = {
              "peliculas": peliculas
       }
       return render(
             request=request,
             template_name= "critica_cine/lista_peliculas.html",
             context = contexto,
       )

        
class PeliculasListView(ListView):
    model = Peliculas
    template_name = "critica_cine/lista_peliculas.html"


class SeriesListView(ListView):
    model = Series
    template_name = "critica_cine/lista_series.html"


class EstrenosListView(ListView):
    model = Proximos_estrenos
    template_name = "critica_cine/lista_estrenos.html"



class PeliculaDetailView(DetailView):
    model = Peliculas
    success_url = reverse_lazy ('peliculas')
    template_name = "critica_cine/detalle_pelicula.html"


class SerieDetailView(DetailView):
    model = Series
    success_url = reverse_lazy ('series')
    template_name = "critica_cine/detalle_serie.html"

class EstrenoDetailView(DetailView):
    model = Proximos_estrenos
    success_url = reverse_lazy ('estrenos')
    template_name = "critica_cine/detalle_estreno.html"


class PeliculasUpdateView(LoginRequiredMixin,UpdateView):
     model = Peliculas
     fields = ['nombre_de_pelicula', 'director', 'pais_de_origen', "descripcion", "fecha_estreno" ]
     success_url = reverse_lazy('peliculas')
     template_name = "critica_cine/pelicula_form.html"

class SeriesUpdateView(LoginRequiredMixin,UpdateView):
     model = Series
     fields = ['nombre_de_pelicula', 'director', 'pais_de_origen', "descripcion",]
     success_url = reverse_lazy('series')
     template_name = "critica_cine/serie_form.html"

class EstrenosUpdateView(LoginRequiredMixin,UpdateView):
     model = Proximos_estrenos
     fields = ['nombre_de_pelicula', 'director', 'pais_de_origen', "descripcion",]
     success_url = reverse_lazy ("estrenos")
     template_name = "critica_cine/estreno_form.html"




class PeliculasDeleteView(LoginRequiredMixin, DeleteView):
     model = Peliculas
     success_url = reverse_lazy('peliculas')
     template_name = "critica_cine/confirmar_eliminacion_pelicula.html"


class SeriesDeleteView(LoginRequiredMixin, DeleteView):
     model = Series
     success_url = reverse_lazy('series')
     template_name = "critica_cine/confirmar_eliminar_serie.html"

class EstrenosDeleteView(LoginRequiredMixin, DeleteView):
     model = Proximos_estrenos
     success_url = reverse_lazy('estrenos')
     template_name = "critica_cine/confirmar_eliminar_estreno.html"


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='critica_cine/registro.html',
        context={'form': formulario},
    )

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='critica_cine/login.html',
        context={'form': form},
    )

class CustomLogoutView(LogoutView):
    template_name = 'critica_cine/logout.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'critica_cine/perfil_formulario.html'

    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
      if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
      else:  # GET
        formulario = AvatarFormulario()
      return render(
        request=request,
        template_name='critica_cine/avatar_formulario.html',
        context={'form': formulario},

      )
    














