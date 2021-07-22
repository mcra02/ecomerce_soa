from django.db import models
from django.contrib.auth.models import  BaseUserManager
#AbstractBaseUser clase abstracta de framework que herada al modelo user de django from
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from simple_history.models import HistoricalRecords

# Create your models here.

#traduce e interactua con la base de datos

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)
 
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email usuario",max_length=200,unique=True, blank = False, null = False)  
    username = models.CharField(max_length = 200, unique = True)
    dni = models.CharField("dni usuario",max_length=200,default = "00000000", blank = False, null = False)  
    name = models.CharField("nombre usuario",max_length=200, blank = False, null = False)  
    last_name = models.CharField("apellido usuario",max_length=200, blank = False, null = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    type_user = models.CharField("tipo de usuario", default = "cajero",max_length=200, blank = False, null = False)
    #objeto encargado de enlazar con el manager
    objects = UserManager()
    historical = HistoricalRecords()    

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
    
    #atributo que no se puede repetir
    USERNAME_FIELD = 'username'
    #cuando creemos usuarios por consola
    REQUIRED_FIELDS = ['email','name','last_name']
    
    def natural_key(self):
        return (self.username)

    def __str__(self):
        return f'{self.name} {self.last_name}'
