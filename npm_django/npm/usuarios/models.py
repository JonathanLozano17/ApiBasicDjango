from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, nombreUsuario, password=None):
        if not nombreUsuario:
            raise ValueError("El usuario debe tener un nombre de usuario no repetido")

        user = self.model(nombreUsuario=nombreUsuario)
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, nombreUsuario, password=None):
        user = self.create_user(nombreUsuario=nombreUsuario, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuarios(AbstractBaseUser):
    nombreUsuario = models.CharField(max_length=255, unique=True)
    
    # Estos campos son requeridos por Django para la autenticación y administración
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nombreUsuario'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nombreUsuario

    @property
    def is_staff(self):
        return self.is_admin

    # Estos métodos son necesarios para que el modelo funcione correctamente con el admin
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    

