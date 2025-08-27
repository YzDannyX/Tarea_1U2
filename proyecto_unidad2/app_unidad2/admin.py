from django.contrib import admin
from .models import Autor, Editorial, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento']
    search_fields = ['nombre', 'apellido']

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais']
    search_fields = ['nombre']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'editorial', 'fecha_publicacion']
    list_filter = ['autor', 'editorial']
    search_fields = ['titulo']