# Create your models here.
"""
run the following commands after creating the models to create the database tables for the models:
python manage.py makemigrations
python manage.py migrate

Asesor:
    Acciones
        Ver empresas
        Ofrecer servicios
        Ver ranking
        Ver noticias
        Ver foros
        Ver certificaciones
    Atributos
        Nombre
        Correo
        Teléfono
        Usuario (Correo)
        Contraseña
        especialidad
        patrocinado (si/no)
        foto de perfil

Empresa:
    Acciones
        Ver servicios (gestión de residuos y contaminación) 
        Solicitar servicios (empresas)
        Ver ranking
        Ver noticias
        Ver foros y comunidad
        Ver capacitaciones y webinars
        Ver asesores
        Solicitar asesoramiento
        Usar autoevaluación
        Ver información y guías sobre certificaciones
        Ver red de proveedores sostenibles
    Atributos
        recompensas de la empresa
        Nombre
        Correo
        Teléfono
        Usuario (Correo)
        Contraseña
        ranking
        certificaciones
        dirección
        número de empleados
        sector (industrial, comercial, etc.)
        logotipo

Certificaciones:
    Atributos
        Nombre
        Descripción
        Requisitos
        Beneficios
        imagen
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_advisor = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    # Add related_name to groups and user_permissions to avoid conflict
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )


# Certification information
class Certification(models.Model):
    name = models.CharField(max_length=100)
    requirements = models.TextField()
    application_process = models.TextField()
    benefits = models.TextField()

# Company profile
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    sustainability_score = models.IntegerField(default=0)
    improvements_needed = models.TextField()

# Supplier network
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    sustainable_products = models.TextField()

# Forum for sharing experiences
class ForumPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
