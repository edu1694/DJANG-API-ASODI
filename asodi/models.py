from django.db import models
import re
from django.forms import ValidationError

# Validador para el formato del RUT
def validate_rut(value):
    # Expresión regular para verificar el formato del RUT: XX.XXX.XXX-X
    rut_pattern = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$')
    if not rut_pattern.match(value):
        raise ValidationError("El formato del RUT es inválido. Debe ser como 11.111.111-1")

# Validador para números no negativos
def validate_positive(value):
    if value < 0:
        raise ValidationError('Este campo no puede ser negativo.')

class Usuario(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, validators=[validate_rut], unique=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    fecha_nacimiento = models.DateField(blank=False)
    correo = models.EmailField(max_length=100,blank=False, unique=True)
    password = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.rut}"

class FichaPersonal(models.Model):
    GENERO_CHOICES = [
        ('M', 'Hombre'),
        ('F', 'Mujer'),
    ]

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, to_field='rut', primary_key=True)
    edad = models.IntegerField(blank=False, validators=[validate_positive])
    estatura = models.FloatField(blank=False, validators=[validate_positive])
    sexo = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=False)
    hospital_perteneciente = models.CharField(max_length=20, blank=False)
    
    # Los siguientes campos son obligatorios
    diabetes = models.BooleanField(default=False)  # True or False
    hipertension = models.BooleanField(default=False)  # True or False
    enfermedad_corazon = models.BooleanField(default=False)  # True or False
    accidente_vascular = models.BooleanField(default=False)  # True or False
    trombosis = models.BooleanField(default=False)  # True or False
    epilepsia = models.BooleanField(default=False)  # True or False
    alergias = models.BooleanField(default=False)  # True or False
    
    numero_contacto = models.IntegerField(blank=False, validators=[validate_positive])

    def __str__(self):
        return f"Ficha de {self.usuario.nombre} {self.usuario.apellido}"

    # Métodos para representar los booleanos como "Sí" o "No"
    def get_diabetes_display(self):
        return "Sí" if self.diabetes else "No"

    def get_hipertension_display(self):
        return "Sí" if self.hipertension else "No"

    def get_enfermedad_corazon_display(self):
        return "Sí" if self.enfermedad_corazon else "No"

    def get_accidente_vascular_display(self):
        return "Sí" if self.accidente_vascular else "No"

    def get_trombosis_display(self):
        return "Sí" if self.trombosis else "No"

    def get_epilepsia_display(self):
        return "Sí" if self.epilepsia else "No"

    def get_alergias_display(self):
        return "Sí" if self.alergias else "No"

class RegistroCitasMedicas(models.Model):
    id_cita_medica = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field='rut')
    fecha = models.DateField(blank=False)
    hora = models.TimeField(blank=False)  # Changed from DATE to TIME for better accuracy
    nombre_medico = models.CharField(max_length=25, blank=False)
    motivo_consulta = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"Cita con {self.nombre_medico} el {self.fecha}"

class RegistroSintoma(models.Model):
    id_registro = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field='rut')
    tipo_sintoma = models.CharField(max_length=15, blank=False)
    descripcion = models.CharField(max_length=50, blank=False)
    fecha_registro = models.DateField(blank=False)

    def __str__(self):
        return f"Síntoma: {self.tipo_sintoma} - {self.descripcion}"

class RegistroPresion(models.Model):
    id_presion = models.AutoField(primary_key=True, default=1)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field='rut')
    presion_diastolica = models.IntegerField(blank=False, validators=[validate_positive])
    presion_sistolica = models.IntegerField(blank=False, validators=[validate_positive])
    frecuenciacardiaca = models.IntegerField(blank=False, validators=[validate_positive])
    fecha_registro = models.DateField(blank=False)

    def __str__(self):
        return f"Presión del {self.fecha_registro}"

class RegistroPeso(models.Model):
    id_peso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field='rut')
    peso = models.IntegerField(blank=False, validators=[validate_positive])
    fecha_registro = models.DateField(blank=False)

    def __str__(self):
        return f"Peso del {self.fecha_registro}"
    
class Anuncios(models.Model):
    id_anuncio = models.AutoField(primary_key=True)
    usuario_asodi = models.ForeignKey('UsuarioAsodi', on_delete=models.CASCADE)
    fecha = models.DateField(blank=False)
    hora = models.TimeField(blank=False)
    titulo = models.CharField(max_length=15, blank=False)
    descripcion = models.TextField(blank=False)
    #imagen = models.ImageField(upload_to='anuncios/')

    def __str__(self):
        return self.titulo

class UsuarioAsodi(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo_electronico = models.EmailField(max_length=100, blank=False, unique=True)
    contraseña = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.correo_electronico
