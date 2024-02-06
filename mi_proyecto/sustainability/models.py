from django.db import models

# Create your models here.
"""
run the following commands after creating the models to create the database tables for the models:
python manage.py makemigrations
python manage.py migrate

Planteamiento:
Información y Guías sobre Certificaciones: Proporcionar información detallada sobre diferentes certificaciones de sostenibilidad en México, como la certificación de Industria Limpia y otras más relevantes. Esto incluiría los requisitos, el proceso de aplicación, y los beneficios de obtener dichas certificaciones.
Asesoramiento Personalizado: Ofrecer asesorías personalizadas para ayudar a las empresas a entender y cumplir con los requisitos específicos de las certificaciones. Esto podría incluir la evaluación de las prácticas actuales de la empresa y la identificación de áreas de mejora.
Gestión de Residuos y Contaminación: Brindar consejos y soluciones para el manejo eficiente de desechos y la reducción de la contaminación. Esto podría incluir la implementación de sistemas de reciclaje, la reducción de emisiones, y la optimización del uso de recursos.
Herramientas de Autoevaluación: Desarrollar herramientas dentro de la app que permitan a las empresas autoevaluar su desempeño en términos de sostenibilidad y entender mejor dónde necesitan mejorar.
Red de Proveedores Sostenibles: Crear una red de proveedores que ofrezcan productos y servicios sostenibles, facilitando a las empresas el acceso a opciones más ecológicas.
Foros y Comunidad: Incluir un espacio para que las empresas puedan compartir experiencias, desafíos y soluciones en el camino hacia la sostenibilidad. Esto fomentaría una comunidad de aprendizaje y apoyo mutuo.
Actualizaciones y Noticias: Mantener a las empresas informadas sobre las últimas tendencias, noticias y cambios en la legislación relacionados con la sostenibilidad y las certificaciones ambientales.
Capacitaciones y Webinars: Ofrecer formaciones en línea sobre temas relevantes para la sostenibilidad empresarial, conducidos por expertos en el campo.
Recompensas a las empresas 
Hacer un ranking de las empresas; mientras más cosas por el ambiente hagas más subes en los lugares (No poner nombres de empresas para no generar competencia directa).
log in como usuario (asesor) y como empresa

Usuarios:
Asesor:
    Ver empresas
    Ofrecer servicios
    Ver ranking
    Ver noticias
    Ver foros
    Ver certificaciones
    Tiene Nombre
    Tiene Correo
    Tiene Teléfono
    Tiene Usuario (Correo)
    Tiene Contraseña
    Tiene especialidad
    Tiene patrocinado (si/no)
    Tiene ranking

Empresa:
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
    Tiene recompensas de la empresa
    Tiene Nombre
    Tiene Correo
    Tiene Teléfono
    Tiene Usuario (Correo)
    Tiene Contraseña
    Tiene ranking
    Tiene certificaciones
    Tiene dirección
    Tiene número de empleados
    Tiene sector
"""

class Asesor(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    patrocinado = models.BooleanField()
    ranking = models.IntegerField()

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    ranking = models.IntegerField()
    certificaciones = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    numero_empleados = models.IntegerField()
    sector = models.CharField(max_length=50)