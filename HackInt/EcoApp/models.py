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
Foro:
    Atributos
        Título
        Contenido
        Empresa
        Fecha de creación
    
        
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_advisor = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

class Certification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField()
    benefits = models.TextField()
    image = models.ImageField(upload_to='certification_images/', blank=True, null=True)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    sustainability_score = models.IntegerField(default=0)
    improvements_needed = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    ranking = models.IntegerField(default=0)
    certifications = models.ManyToManyField(Certification, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number_of_employees = models.IntegerField(default=0)
    sector = models.CharField(max_length=255, blank=True, null=True) 

class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='advisor')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    specialty = models.CharField(max_length=255)
    sponsored = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='advisor_profile_pictures/', blank=True, null=True)

class ForumPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='forum_posts')
    created_at = models.DateTimeField(auto_now_add=True)
