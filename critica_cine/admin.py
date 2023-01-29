from django.contrib import admin

from critica_cine.models import Peliculas, Series, Proximos_estrenos, Valoracion_cine, Valoracion_serie


# Register your models here.
admin.site.register(Peliculas)
admin.site.register(Series)
admin.site.register(Valoracion_cine)
admin.site.register(Valoracion_serie)
admin.site.register(Proximos_estrenos)
