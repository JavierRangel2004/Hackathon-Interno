from django.db import models

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

class Advisor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    sponsored = models.BooleanField()
    profile_picture = models.ImageField()

class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    ranking = models.IntegerField()
    certifications = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    employees = models.IntegerField()
    sector = models.CharField(max_length=50)
    logo = models.ImageField()

class Certification(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    requirements = models.TextField()
    benefits = models.TextField()
    image = models.ImageField()
