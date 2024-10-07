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
    
# Modelo para UsuarioAsodiAdmin
class UsuarioAsodiAdmin(models.Model):
    correo = models.EmailField(max_length=50, unique=True, blank=False, primary_key=True)
    password = models.CharField(max_length=50, blank=False)
    nombre = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.correo

# Modelo para UsuarioAsodiAd
class UsuarioAsodiAd(models.Model):
    rut_ad  = models.CharField(max_length=12, primary_key=True, validators=[validate_rut], unique=True)
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    correo = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    estado_ad = models.BooleanField(default=True)  # Asumo que es un campo booleano de estado activo/inactivo

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para Convenios
class Convenios(models.Model):
    nombre_convenio = models.CharField(max_length=50, primary_key=True)
    horas_llamado = models.IntegerField(validators=[validate_positive])
    dias_para_operar = models.IntegerField(validators=[validate_positive])
    dias_para_alertar = models.IntegerField(validators=[validate_positive])
    usuario_asodi_admin = models.ForeignKey(UsuarioAsodiAdmin, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_convenio

class PlanillasConvenio(models.Model):
    ESTADO_PACIENTE_CHOICES = [
        ('P', 'Pendiente'),
        ('E', 'En proceso'),
        ('O', 'Operado'),
        ('A', 'Alta'),
        ('R', 'Rechazado'),
    ]

    id_planilla = models.AutoField(primary_key=True)
    fecha_recepcion = models.DateTimeField(auto_now_add=True)  # Esto guardará la fecha y hora de creación
    rut = models.CharField(max_length=12, validators=[validate_rut], unique=True)
    nombre_paciente = models.CharField(max_length=50, blank=False)
    apellido_paciente = models.CharField(max_length=50, blank=False)
    fecha_sic = models.DateField(blank=True, null=True)
    reg_primer_llamado = models.DateField(blank=False)
    reg_segundo_llamado = models.DateField(blank=True, null=True)
    reg_tercer_llamado = models.DateField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    doctor = models.CharField(max_length=50, blank=True, null=True)
    fecha_evaluacion = models.DateField(blank=True, null=True)
    fecha_cirugia = models.DateField(blank=True, null=True)
    control_post_operatorio = models.DateField(blank=True, null=True)
    control_mes = models.DateField(blank=True, null=True)
    
    estado_paciente = models.CharField(
        max_length=1,
        choices=ESTADO_PACIENTE_CHOICES,
        default='P',
        blank=False
    )
    
    motivo_rechazo = models.TextField(blank=True, null=True)
    convenios = models.ForeignKey('Convenios', on_delete=models.CASCADE)
    usuario_asodi_ad = models.ForeignKey('UsuarioAsodiAd', on_delete=models.CASCADE)

    def clean(self):
        if self.estado_paciente == 'R' and not self.motivo_rechazo:
            raise ValidationError("Debes proporcionar un motivo de rechazo si el estado es 'Rechazado'.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Planilla del paciente {self.nombre_paciente} {self.apellido_paciente}"




# Modelo para Anuncios
class Anuncios(models.Model):
    id_anuncio = models.AutoField(primary_key=True)
    usuario_asodi_admin = models.ForeignKey('UsuarioAsodiAdmin', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, blank=False)
    descripcion = models.TextField(blank=False)
    fecha_inicio = models.DateField(blank=False)
    fecha_termino = models.DateField(blank=False)
    estado_an = models.BooleanField(default=True)  # Campo para indicar si el anuncio está activo o inactivo
    imagen = models.ImageField(upload_to='anuncios/', blank=True, null=True)  # Campo opcional para la imagen

    def __str__(self):
        return self.titulo
    
class Solicitudes(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('A', 'Aprobada'),
        ('R', 'Rechazada'),
    ]

    id_soli = models.AutoField(primary_key=True)
    motivo = models.TextField(blank=False)
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,
        default='P'  # Pendiente por defecto
    )
    fecha_creacion = models.DateField(auto_now_add=True)
    planilla_convenio = models.ForeignKey(PlanillasConvenio, on_delete=models.CASCADE)  # Relación con la planilla de convenios
    usuario_solicitante = models.ForeignKey(UsuarioAsodiAd, on_delete=models.CASCADE)  # Usuario solicitante (UsuarioAsodiAd)
    
    def str(self):
        return f"Solicitud {self.id_soli} - {self.estado}"