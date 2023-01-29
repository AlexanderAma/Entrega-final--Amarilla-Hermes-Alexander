from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from critica_cine.models import Avatar

class Peliculaformulario(forms.Form):
    nombre_de_pelicula = forms.CharField(max_length=200)
    director = forms.CharField(max_length=200)
    pais_de_origen = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=500)
    fecha_estreno = forms.DateField()

class Serieformulario(forms.Form):
    nombre_de_pelicula = forms.CharField(max_length=200)
    director = forms.CharField(max_length=200)
    pais_de_origen = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=500)
    plataforma= forms.CharField()


class Estrenosformulario(forms.Form):
    nombre_de_pelicula = forms.CharField(max_length=200)
    director = forms.CharField(max_length=200)
    pais_de_origen = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=500)

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields =["last_name", "first_name", "email"]


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']



