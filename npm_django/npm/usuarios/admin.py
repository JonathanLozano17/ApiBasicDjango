from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from usuarios.models import Usuarios

@admin.register(Usuarios)
class UsuarioAdmin(BaseUserAdmin):
    list_display = ('nombreUsuario', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('nombreUsuario', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombreUsuario', 'password1', 'password2', 'is_active', 'is_admin'),
        }),
    )
    search_fields = ('nombreUsuario',)
    ordering = ('nombreUsuario',)
    filter_horizontal = ()
