from django.db import models
from django.contrib.auth.models import User
#-------------------------------------------------------------------------------------------------
#-----------------------------------------Nivel de Enseñanza--------------------------------------
#-------------------------------------------------------------------------------------------------
NIVEL2_CHOICE=[
    ('BASICA','BASICA'),
    ('MEDIA','MEDIA'),
    ('BASICA y MEDIA','BASICA y MEDIA')
]
#-------------------------------------------------------------------------------------------------
#-----------------------------------------Asignaturas---------------------------------------------
#-------------------------------------------------------------------------------------------------
ASIGNATURA_CHOICE=[
    ('Artes (3ero y 4to Medio) - 2hrs','Artes (3ero y 4to Medio) - 2hrs'),
    ('Artes Visuales (1ero a 4to Basico) - 2hrs','Artes Visuales (1ero a 4to Basico) - 2hrs'),
    ('Artes Visuales (5to a 6to Basico) - 1hr','Artes Visuales (5to a 6to Basico) - 1hr'),
    ('Artes Visuales o Música (1ero y 2do Medio) - 2hrs','Artes Visuales o Música (1ero y 2do Medio) - 2hrs'),
    ('Artes Visuales y Música (7mo y 8vo Basico) - 2hrs','Artes Visuales y Música (7mo y 8vo Basico) - 2hrs'),
    ('Asignatura Kinder - 1hr','Asignatura Kinder - 1hr'),
    ('Asignatura PreKinder - 1hr','Asignatura PreKinder - 1hr'),
    ('Ciencias Naturales  (1ero y 2do Medio) - 6hrs','Ciencias Naturales  (1ero y 2do Medio) - 6hrs'),
    ('Ciencias Naturales  (7mo y 8vo Basico) - 4hrs','Ciencias Naturales  (7mo y 8vo Basico) - 4hrs'),
    ('Ciencias Naturales (1ero a 6to Basico) - 3hrs','Ciencias Naturales (1ero a 6to Basico) - 3hrs'),
    ('Ciencias para la Ciudadanía (3ero y 4to Medio) - 2hrs','Ciencias para la Ciudadanía (3ero y 4to Medio) - 2hrs'),
    ('Educación Ciudadana (3ero y 4to Medio) - 2hrs','Educación Ciudadana (3ero y 4to Medio) - 2hrs'),
    ('Educación Física y Salud  (Todas) - 2hrs','Educación Física y Salud  (Todas) - 2hrs'),
    ('Electivo de biología (3ero y 4to Medio) - 6hrs','Electivo de biología (3ero y 4to Medio) - 6hrs'),
    ('Electivo de matematicas (3ero y 4to Medio) - 6hrs','Electivo de matematicas (3ero y 4to Medio) - 6hrs'),
    ('Electivo de historia (3ero y 4to Medio) - 6hrs','Electivo de historia (3ero y 4to Medio) - 6hrs'),
    ('Electivo de lengua y literatura (3ero y 4to Medio) - 6hrs','Electivo de lengua y literatura (3ero y 4to Medio) - 6hrs'),
    ('Filosofía (3ero y 4to Medio) - 2hrs','Filosofía (3ero y 4to Medio) - 2hrs'),
    ('Historia, Geografía y Ciencias Sociales  (5to a 2do Medio) - 4hrs','Historia, Geografía y Ciencias Sociales  (5to a 2do Medio) - 4hrs'),
    ('Historia, Geografía y Ciencias Sociales (1ero a 4to Basico) - 3hrs','Historia, Geografía y Ciencias Sociales (1ero a 4to Basico) - 3hrs'),
    ('Historia, Geografía y Ciencias Sociales (3ero y 4to Medio) - 2hrs','Historia, Geografía y Ciencias Sociales (3ero y 4to Medio) - 2hrs'),
    ('Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs','Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs'),
    ('Inglés (3ero y 4to Medio) - 2hrs','Inglés (3ero y 4to Medio) - 2hrs'),
    ('Inglés (Libre Disposicion)  (1ero a 4to Basico) - 1hr','Inglés (Libre Disposicion)  (1ero a 4to Basico) - 1hr'),
    ('Inglés Nivel Transicion (Prekinder y Kinder) - 1hr','Inglés Nivel Transicion (Prekinder y Kinder) - 1hr'),
    ('Lengua y Literatura (3ero y 4to Medio) - 3hrs','Lengua y Literatura (3ero y 4to Medio) - 3hrs'),
    ('Lengua y Literatura (7mo a 2do Medio) - 6hrs','Lengua y Literatura (7mo a 2do Medio) - 6hrs'),
    ('Lenguaje y Comunicación  (5to y 6to Basico) - 6hrs','Lenguaje y Comunicación  (5to y 6to Basico) - 6hrs'),
    ('Lenguaje y Comunicación (1ero a 4to Basico) - 8hrs','Lenguaje y Comunicación (1ero a 4to Basico) - 8hrs'),
    ('Matemática  (1ero Basico a 2do Medio) - 6hrs','Matemática  (1ero Basico a 2do Medio) - 6hrs'),
    ('Matemática  (3ero y 4to Medio) - 3hrs','Matemática  (3ero y 4to Medio) - 3hrs'),
    ('Música  (1ero a 4to Basico) - 2hrs','Música  (1ero a 4to Basico) - 2hrs'),
    ('Música  (5to y 6to Basico) - 1hr','Música  (5to y 6to Basico) - 1hr'),
    ('Orientación  (1ero a 4to Basico) - 1hr','Orientación  (1ero a 4to Basico) - 1hr'),
    ('Orientación  (5to a 2do Medio) - 1hr','Orientación  (5to a 2do Medio) - 1hr'),
    ('Religión (Todas) - 2hrs','Religión (Todas) - 2hrs'),
    ('Tecnología  (1ero a 4to Basico) - 1hr','Tecnología  (1ero a 4to Basico) - 1hr'),
    ('Tecnología  (5to a 2do Medio) - 1hr','Tecnología  (5to a 2do Medio) - 1hr'),
]
#-------------------------------------------------------------------------------------------------
#-----------------------------------------Nivel de Asignaturas------------------------------------
#-------------------------------------------------------------------------------------------------
NIVEL_CHOICE=[
    ('BASICA','BASICA'),
    ('MEDIA','MEDIA'),
    ('PREBASICA','PREBASICA')
]
#-------------------------------------------------------------------------------------------------
#------------------------------Dias Horario y Disponibilidad--------------------------------------
#-------------------------------------------------------------------------------------------------
DIA_CHOICE=[
    ('LUNES','LUNES'),
    ('MARTES','MARTES'),
    ('MIERCOLES','MIERCOLES'),
    ('JUEVES','JUEVES'),
    ('VIERNES','VIERNES'),
]
#-------------------------------------------------------------------------------------------------
#---------------------------Bloques Horario y Disponibilidad--------------------------------------
#-------------------------------------------------------------------------------------------------
BLOQUE_CHOICE=[
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
]
#-------------------------------------------------------------------------------------------------
#------------------------------------Estado Disponibilidad----------------------------------------
#-------------------------------------------------------------------------------------------------
ESTADO_CHOICE=[
    ('DISPONIBLE','DISPONIBLE'),
    ('NO DISPONIBLE','NO DISPONIBLE'),
]
#-------------------------------------------------------------------------------------------------
#---------------------------------------Lista de Cursos-------------------------------------------
#-------------------------------------------------------------------------------------------------
CURSOS_CHOICE=[
    ("PREKINDER", "PREKINDER"),
    ("KINDER", "KINDER"),
    ('PRIMERO BASICO','PRIMERO BASICO'),
    ('SEGUNDO BASICO','SEGUNDO BASICO'),
    ('TERCERO BASICO','TERCERO BASICO'),
    ('CUARTO BASICO','CUARTO BASICO'),
    ('QUINTO BASICO','QUINTO BASICO'),
    ('SEXTO BASICO','SEXTO BASICO'),
    ('SEPTIMO BASICO','SEPTIMO BASICO'),
    ('OCTAVO BASICO','OCTAVO BASICO'),
    ('PRIMERO MEDIO','PRIMERO MEDIO'),
    ('SEGUNDO MEDIO','SEGUNDO MEDIO'),
    ('TERCERO MEDIO','TERCERO MEDIO'),
    ('CUARTO MEDIO','CUARTO MEDIO'),
]
#-------------------------------------------------------------------------------------------------
#---------------------------------Lista Cursos Repetidos------------------------------------------
#-------------------------------------------------------------------------------------------------
CURSOSR_CHOICE=[
    ('NO APLICA','NO APLICA'),
    ("PREKINDER", "PREKINDER"),
    ("KINDER", "KINDER"),
    ('PRIMERO BASICO','PRIMERO BASICO'),
    ('SEGUNDO BASICO','SEGUNDO BASICO'),
    ('TERCERO BASICO','TERCERO BASICO'),
    ('CUARTO BASICO','CUARTO BASICO'),
    ('QUINTO BASICO','QUINTO BASICO'),
    ('SEXTO BASICO','SEXTO BASICO'),
    ('SEPTIMO BASICO','SEPTIMO BASICO'),
    ('OCTAVO BASICO','OCTAVO BASICO'),
    ('PRIMERO MEDIO','PRIMERO MEDIO'),
    ('SEGUNDO MEDIO','SEGUNDO MEDIO'),
    ('TERCERO MEDIO','TERCERO MEDIO'),
    ('CUARTO MEDIO','CUARTO MEDIO'),
]
#-------------------------------------------------------------------------------------------------
#---------------------------------Comunas de la Region de O'higgins--------------------------------------
#-------------------------------------------------------------------------------------------------
COMUNA_CHOISE=[
    ('Antofagasta','Antofagasta'),
    ('Buin','Buin'),
    ('Calama','Calama'),
    ('Chépica','Chépica'),
    ('Chimbarongo','Chimbarongo'),
    ('Codegua','Codegua'),
    ('Coinco','Coinco'),
    ('Coltauco','Coltauco'),
    ('Colina','Colina'),
    ('Doñihue','Doñihue'),
    ('Graneros','Graneros'),
    ('Huechuraba','Huechuraba'),
    ('Isla de Maipo','Isla de Maipo'),
    ('Lampa','Lampa'),
    ('La Estrella','La Estrella'),
    ('Las Cabras','Las Cabras'),
    ('Litueche','Litueche'),
    ('Lolol','Lolol'),
    ('Lo Espejo','Lo Espejo'),
    ('Maipu','Maipu'),
    ('Machalí','Machalí'),
    ('Malloa','Malloa'),
    ('Marchihue','Marchihue'),
    ('Mostazal','Mostazal'),
    ('Nancagua','Nancagua'),
    ('Navidad','Navidad'),
    ('Olivar','Olivar'),
    ('Palmilla','Palmilla'),
    ('Paredones','Paredones'),
    ('Peralillo','Peralillo'),
    ('Peumo','Peumo'),
    ('Peñalolén','Peñalolén'),
    ('Pichidegua','Pichidegua'),
    ('Pichilemu','Pichilemu'),
    ('Placilla','Placilla'),
    ('Pumanque','Pumanque'),
    ('Quinta de Tilcoco','Quinta de Tilcoco'),
    ('Rancagua','Rancagua'),
    ('Renca','Renca'),
    ('Rengo','Rengo'),
    ('Requínoa','Requínoa'),
    ('San Fernando','San Fernando'),
    ('Santa Cruz','Santa Cruz'),
    ('San Vicente','San Vicente'),
    ('San Rosendo','San Rosendo'),
    ('Santiago','Santiago'),
    ('San Bernardo','San Bernardo'),
    ('San Carlos','San Carlos'),
]
#-------------------------------------------------------------------------------------------------
#---------------------------------------Opciones Prevision----------------------------------------
#-------------------------------------------------------------------------------------------------
PREVISION_CHOISE=[
    ('Isapre','Isapre'),
    ('Fonasa','Fonasa'),
    ('Ninguna','Ninguna'),
]
#-------------------------------------------------------------------------------------------------
#----------------------------------------Letras Fonasa--------------------------------------------
#-------------------------------------------------------------------------------------------------
FONASA_CHOICE=[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('NO APLICA','NO APLICA'),
]
#-------------------------------------------------------------------------------------------------
#---------------------------------------Opciones Simples------------------------------------------
#-------------------------------------------------------------------------------------------------
ALIMENTACION_CHOICE=[
    ('Si','Si'),
    ('No','No'),
    ('No sabe','No sabe'),
]
#-------------------------------------------------------------------------------------------------
#--------------------------------------Niveles de Escolaridad-------------------------------------
#-------------------------------------------------------------------------------------------------
ESCOLARIDAD_CHOICE=[
    ("SIN ESTUDIOS", "SIN ESTUDIOS"),
    ("BASICA INCOMPLETA", "BASICA INCOMPLETA"),
    ("BASICA COMPLETA", "BASICA COMPLETA"),
    ("MEDIA INCOMPLETA", "MEDIA INCOMPLETA"),
    ("MEDIA COMPLETA", "MEDIA COMPLETA"),
    ("ESTUDIOS SUPERIORES INCOMPLETA", "ESTUDIOS SUPERIORES INCOMPLETA"),
    ("ESTUDIOS SUPERIORES COMPLETA", "ESTUDIOS SUPERIORES COMPLETA"),
]
#-------------------------------------------------------------------------------------------------
#----------------------------------------Opciones de Actividades----------------------------------
#-------------------------------------------------------------------------------------------------
TIPOACTIVIDAD_CHOICES = [
    ('ACT. RECREATIVA', "ACT. RECREATIVA"),
    ('ACT. DE BAILE', "ACT. DE BAILE"),
    ('ACT. DEPORTIVA', "ACT. DEPORTIVA"),
    ('OTRA ACTIVIDAD', "OTRA ACTIVIDAD"),
]
#-------------------------------------------------------------------------------------------------
#------------------------------------Opciones de Atenciones---------------------------------------
#-------------------------------------------------------------------------------------------------
TIPOATENCION_CHOICES = (
    ('ATENCION MEDICA O ENFERMERIA', "ATENCION MEDICA O ENFERMERIA"),
    ('ATENCION NUTRICIONAL', "ATENCION NUTRICIONAL"),
    ('ATENCION PSICOPEDAGOGICA', "ATENCION PSICOPEDAGOGICA"),
    ('ATENCION SOCIAL', "ATENCION SOCIAL"),
    ('ORIENTACION VOCACIONAL', "ORIENTACION VOCACIONAL"),
    ('PSICOLOGICA', "PSICOLOGICA"),
    ('PEDAGOGICA', "PEDAGOGICA"),
)
#-------------------------------------------------------------------------------------------------
#--------------------------------------Estados de Insumos-----------------------------------------
#-------------------------------------------------------------------------------------------------
ESTADOINSUMO_CHOICES = (
    ("BUENO", "BUENO"),
    ("MALO", "MALO"),
    ("EN REPARACION", "EN REPARACION"),
)
#-------------------------------------------------------------------------------------------------
#----------------------------------------Estados de Prestamos-------------------------------------
#-------------------------------------------------------------------------------------------------
ESTADOPRESTAMO_CHOICES = (
    ("SIN DEVOLVER", "SIN DEVOLVER"),
    ("DEVUELTO", "DEVUELTO"),
)
#-------------------------------------------------------------------------------------------------
#---------------------------------------Estado de Certificados------------------------------------
#-------------------------------------------------------------------------------------------------
ESTADOCERTIFICADO_CHOICES = (
    ("RETIRADO", "RETIRADO"),
    ("SIN ENTREGAR", "SIN ENTREGAR"),
    ("PENDIENTE", "PENDIENTE"),
)
#-------------------------------------------------------------------------------------------------
#---------------------------------------Estado de Impresiones-------------------------------------
#-------------------------------------------------------------------------------------------------
ESTADOIMPRESION_CHOICES = (
    ("REALIZADO", "REALIZADO"),
    ("PENDIENTE", "PENDIENTE"),
    ("ERROR", "ERROR"),
)
#-------------------------------------------------------------------------------------------------
#---------------------------------------Tipos de Certificados-------------------------------------
#-------------------------------------------------------------------------------------------------
TIPOCERTIFICADO_CHOICES = (
    ("CERTIFICADO DE ENSEÑANZA BASICA", "CERTIFICADO DE ENSEÑANZA BASICA"),
    ("CERTIFICADO DE ENSEÑANZA MEDIA", "CERTIFICADO DE ENSEÑANZA MEDIA"),
    ("CERTIFICADO DE ALUMNO REGULAR", "CERTIFICADO DE ALUMNO REGULAR"),
    ("CERTIFICADO DE CONDUCTA", "CERTIFICADO DE CONDUCTA"),
    ("CERTIFICADO DE PARTICIPACION EN ACTIVIDADES EXTRACURRICULARES", "CERTIFICADO DE PARTICIPACION EN ACTIVIDADES EXTRACURRICULARES"),
)
#-------------------------------------------------------------------------------------------------
#------------------------------------------Razon de Atenciones------------------------------------
#-------------------------------------------------------------------------------------------------
MOTIVOATENCION_CHOICES = (
    ('CITACION', "CITACION"),
    ('DESCONPENSACION', "DESCONPENSACION"),
    ('URGENCIA', "URGENCIA"),
    ('SOLICITUD', "SOLICITUD"),
    ('OTRA', "OTRA"),
)
#-------------------------------------------------------------------------------------------------
#---------------------------------------Modelo Profesores-----------------------------------------
#-------------------------------------------------------------------------------------------------
class Profesor(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    rut=models.TextField(max_length=100,unique=True)
    nombre=models.TextField(max_length=100)
    apellido=models.TextField(max_length=100)
    nivel=models.CharField(max_length=16,default='BASICA y MEDIA')
    email=models.EmailField(unique=True)
    Foto = models.ImageField(upload_to="images/profesores/",null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.Foto:
            self.Foto = 'images/profesores/sinimagen.png'

        super(Profesor, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.rut} / {self.nombre} {self.apellido}"
#-------------------------------------------------------------------------------------------------
#---------------------------------------------Modelo de Cursos------------------------------------
#-------------------------------------------------------------------------------------------------
class Curso(models.Model):
    nombre=models.TextField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"
#-------------------------------------------------------------------------------------------------
#----------------------------------------Modelo de Asignaturas------------------------------------
#-------------------------------------------------------------------------------------------------
class Asignatura(models.Model):
    codigo=models.TextField(max_length=100)
    nombre=models.CharField(max_length=100,choices=ASIGNATURA_CHOICE)
    nivel=models.CharField(max_length=100,choices=NIVEL_CHOICE)
    bloques=models.IntegerField(null=False)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo} / {self.nombre} / {self.curso.nombre}"
#-------------------------------------------------------------------------------------------------
#---------------------------------------Modelo de Especilidades-----------------------------------
#-------------------------------------------------------------------------------------------------
class AsignaturasProfesor(models.Model):
    nombre=models.CharField(max_length=100,choices=ASIGNATURA_CHOICE)
    nivel=models.TextField(max_length=100,default='BASICA y MEDIA')
    profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE)
#-------------------------------------------------------------------------------------------------
#---------------------------------------Modelo de Disponibilid------------------------------------
#-------------------------------------------------------------------------------------------------
class DisponibilidadProfesor(models.Model):
    bloque=models.IntegerField(null=False,choices=BLOQUE_CHOICE)
    dia=models.TextField(max_length=100,choices=DIA_CHOICE)
    estado=models.TextField(max_length=100,default="NO DISPONIBLE",choices=ESTADO_CHOICE)
    profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE)
#-------------------------------------------------------------------------------------------------
#--------------------------------Modelo de Horarios (Cursos y Profesores)-------------------------
#-------------------------------------------------------------------------------------------------
class Horario(models.Model):
    bloque=models.IntegerField(null=False,choices=BLOQUE_CHOICE)
    dia=models.TextField(max_length=100,choices=DIA_CHOICE)
    asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE, null=True)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE, null=True)
#-------------------------------------------------------------------------------------------------
#----------------------------------Modelos Usuarios de templates----------------------------------
#-------------------------------------------------------------------------------------------------
class Usuario(models.Model):
    nombre=models.TextField(max_length=100)
    password=models.TextField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"
#-------------------------------------------------------------------------------------------------
#-----------------------------Modelo de Historial de Acciones en templates------------------------
#-------------------------------------------------------------------------------------------------
class Historial(models.Model):
    fecha=models.DateTimeField()
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    accion=models.TextField(max_length=200)
    tabla=models.TextField(max_length=100)
#-------------------------------------------------------------------------------------------------
#-------------------------------------Modelo de Alumnos-------------------------------------------
#-------------------------------------------------------------------------------------------------
class Alumnos(models.Model):
    matricula=models.IntegerField(primary_key=True,unique=True)
    Administrativo = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    FechaHoraRegistroMatriculaEstudiante = models.DateTimeField(blank=True, auto_now_add=True)
    curso=models.CharField(max_length=50,choices=CURSOS_CHOICE)
    run=models.CharField(max_length=12,blank=False,unique=True)
    nombre=models.CharField(max_length=100,blank=False)
    apellido_paterno=models.CharField(max_length=50,blank=False)
    apellido_materno=models.CharField(max_length=50,blank=False)
    direccion=models.CharField(max_length=200,blank=False,default='-----')
    comuna=models.CharField(max_length=50,choices=COMUNA_CHOISE)
    procedencia=models.CharField(max_length=150,default='-----',null=True)
    curso_repetido=models.CharField(max_length=50,choices=CURSOSR_CHOICE,default='NO APLICA')
    con_quien_vive=models.CharField(max_length=100,blank=False,default='-----')
    enfermedad=models.CharField(max_length=120,null=True,default='-----')
    prevision=models.CharField(max_length=20,choices=PREVISION_CHOISE,blank=False,default='Ninguna')
    letra_fonasa=models.CharField(max_length=10,choices=FONASA_CHOICE,blank=False,default='NO APLICA')
    alimentacion_establecimiento=models.CharField(max_length=8,choices=ALIMENTACION_CHOICE,blank=False,default='No sabe')
    programa_solidario=models.CharField(max_length=7,choices=ALIMENTACION_CHOICE,blank=False,default='No sabe')
    programa=models.CharField(max_length=150,default='-----',null=True)
    locomocion=models.CharField(max_length=50,blank=False,default='-----')
    fono_locomocion=models.CharField(max_length=9,default='9',null=True)
    vive_con=models.CharField(max_length=150,blank=False,default='-----')
    emergencia=models.CharField(max_length=50,blank=False,default='-----')
    complementarios=models.CharField(max_length=200,blank=True)
    Foto = models.ImageField(upload_to="images/estudiantes/",null=True,blank=True)

    def save(self, *args, **kwargs):


        if not self.Foto:
            self.Foto = 'images/estudiantes/sinimagen.png'

        super(Alumnos, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno} {self.nombre} / {self.curso}"
#-------------------------------------------------------------------------------------------------
#---------------------------------------Modelo de Padres------------------------------------------
#-------------------------------------------------------------------------------------------------
class Padre(models.Model):
    alumno=models.ForeignKey(Alumnos,on_delete=models.CASCADE, related_name="Padres")
    es_madre=models.BooleanField()
    run=models.CharField(max_length=12,blank=True)
    nombre=models.CharField(max_length=100,blank=True)
    apellido_paterno=models.CharField(max_length=50,blank=True)
    apellido_materno=models.CharField(max_length=50,blank=True)
    fono=models.CharField(max_length=9,default='9',blank=True)
    escolaridad=models.CharField(max_length=32,choices=ESCOLARIDAD_CHOICE,blank=True)
    ocupacion=models.CharField(max_length=100,default='No aplica',blank=True)
    edad=models.IntegerField(blank=True)
    religion=models.CharField(max_length=20,default='No aplica',blank=True)
#-------------------------------------------------------------------------------------------------
#-----------------------------------------Modelo de Apoderados------------------------------------
#-------------------------------------------------------------------------------------------------
class Apoderado(models.Model):
    alumno=models.ForeignKey(Alumnos,on_delete=models.CASCADE, related_name="Apoderados")
    run=models.CharField(max_length=12,blank=True)
    nombre=models.CharField(max_length=100,blank=True)
    apellido_paterno=models.CharField(max_length=50,blank=True)
    apellido_materno=models.CharField(max_length=50,blank=True)
    fono=models.CharField(max_length=9,default='9',blank=True)
    escolaridad=models.CharField(max_length=32,choices=ESCOLARIDAD_CHOICE,blank=True)
    ocupacion=models.CharField(max_length=100,default='No aplica',blank=True)
    edad=models.IntegerField(blank=True)
    religion=models.CharField(max_length=20,default='No aplica',blank=True)
#-------------------------------------------------------------------------------------------------
#--------------------------------------Modelo de Actividades--------------------------------------
#-------------------------------------------------------------------------------------------------
class Actividades(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    Tipo = models.CharField(max_length=50, choices=TIPOACTIVIDAD_CHOICES,blank=False)
    Profesor = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    Nombre = models.CharField(max_length=200, blank=True)
    FechaHoraRegistro = models.DateTimeField(blank=True, auto_now_add=True)
    FechaHoraPlanificada = models.DateTimeField(blank=True)
    Observacion = models.TextField(max_length=100, blank=False)
    Foto1 = models.FileField(upload_to="images/actividades/",null=True,blank=True)
    Foto2 = models.FileField(upload_to="images/actividades/",null=True,blank=True)
    Foto3 = models.FileField(upload_to="images/actividades/",null=True,blank=True)
    NumeroParticipantesActividad = models.IntegerField(default = 0,blank=False)

    def save(self, *args, **kwargs):

        if not self.Foto1:
            self.Foto1 = 'images/actividades/sinimagen.png'
        if not self.Foto2:
            self.Foto2 = 'images/actividades/sinimagen.png'
        if not self.Foto3:
            self.Foto3 = 'images/actividades/sinimagen.png'

        super(Actividades, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} / {self.Nombre}"
#-------------------------------------------------------------------------------------------------
#---------------------------------------Modelo de Atenciones--------------------------------
#-------------------------------------------------------------------------------------------------
class Atenciones(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    Tipo = models.CharField(max_length=50, choices=TIPOATENCION_CHOICES,blank=False)
    Profesional = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    FechaHoraRegistro = models.DateTimeField(blank=True, auto_now_add=True)
    idMatricula = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    Motivo = models.TextField(max_length=100, choices=MOTIVOATENCION_CHOICES, blank=False)
    Observaciones = models.TextField(blank=False)
    Foto1Evidencia = models.FileField(upload_to="images/atenciones/",null=True,blank=True)
    Foto2Evidencia = models.FileField(upload_to="images/atenciones/",null=True,blank=True)
    Foto3Evidencia = models.FileField(upload_to="images/atenciones/",null=True,blank=True)

    def save(self, *args, **kwargs):

        if not self.Foto1Evidencia:
            self.Foto1Evidencia = 'images/atenciones/sinimagen.png'
        if not self.Foto2Evidencia:
            self.Foto2Evidencia = 'images/atenciones/sinimagen.png'
        if not self.Foto3Evidencia:
            self.Foto3Evidencia = 'images/atenciones/sinimagen.png'

        super(Atenciones, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} / {self.idMatricula.apellido_paterno} {self.idMatricula.apellido_materno} {self.idMatricula.nombre}"
#-------------------------------------------------------------------------------------------------
#-----------------------------------------Modelo de Insumos---------------------------------------
#-------------------------------------------------------------------------------------------------
class Insumos(models.Model):
    IdInsumo = models.AutoField(primary_key=True, auto_created=True)
    NombreInsumo = models.CharField(max_length=100, blank=False)
    DetalleInsumo = models.TextField(max_length=100, blank=False)
    StockInsumo = models.IntegerField(default = 0,blank=False)
    Foto1Insumo = models.FileField(upload_to="images/insumos/",null=True,blank=True)
    Foto2Insumo = models.FileField(upload_to="images/insumos/",null=True,blank=True)
    Foto3Insumo = models.FileField(upload_to="images/insumos/",null=True,blank=True)
    EstadoInsumo = models.CharField(max_length=50, choices=ESTADOINSUMO_CHOICES,blank=False)

    def save(self, *args, **kwargs):
        if not self.Foto1Insumo:
            self.Foto1Insumo = 'images/insumos/sinimagen.png'
        if not self.Foto2Insumo:
            self.Foto2Insumo = 'images/insumos/sinimagen.png'
        if not self.Foto3Insumo:
            self.Foto3Insumo = 'images/insumos/sinimagen.png'

        super(Insumos, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.IdInsumo} / {self.NombreInsumo}"
#-------------------------------------------------------------------------------------------------
#----------------------------------------Modelo de Prestamos--------------------------------------
#-------------------------------------------------------------------------------------------------
class Prestamos(models.Model):
    IdPrestamo = models.AutoField(primary_key=True, auto_created=True)
    Administrativo = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    FechaHoraRegistroPrestamo = models.DateTimeField(blank=True, auto_now_add=True)
    FechaHoraDevolucionPrestamo = models.DateTimeField(blank=True)
    DetallePrestamo = models.TextField(max_length=100, blank=False)
    FotoPrestamo = models.FileField(upload_to="images/prestamos/",null=True,blank=True)
    EstadoPrestamo = models.CharField(max_length=50, choices=ESTADOPRESTAMO_CHOICES,blank=False, default="SIN DEVOLVER")

    def save(self, *args, **kwargs):

        if not self.FotoPrestamo:
            self.FotoPrestamo = 'images/prestamos/sinimagen.png'

        super(Prestamos, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.IdPrestamo} / {self.Administrativo.last_name} {self.Administrativo.first_name}"
#-------------------------------------------------------------------------------------------------
#---------------------------------------Modelo de Certificados------------------------------------
#-------------------------------------------------------------------------------------------------
class Certificados(models.Model):
    idCertificado = models.AutoField(primary_key=True, auto_created=True)
    idMatricula = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    TipoCertificado = models.CharField(max_length=100, choices=TIPOCERTIFICADO_CHOICES,blank=False)
    MotivoCertificado = models.CharField(max_length=200, blank=False)
    LugarPresentacionCertificado = models.CharField(max_length=200, blank=False)
    Administrativo = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    FechaHoraRegistroCertificado = models.DateTimeField(blank=True, auto_now_add=True)
    EstadoCertificado = models.CharField(max_length=50, choices=ESTADOCERTIFICADO_CHOICES,blank=False, default="PENDIENTE")

    def __str__(self):
        return f"{self.idCertificado} / {self.idMatricula.apellido_paterno} {self.idMatricula.apellido_materno} {self.idMatricula.nombre}"
#-------------------------------------------------------------------------------------------------
#---------------------------------------Modelo de Consejo de Profesores---------------------------
#-------------------------------------------------------------------------------------------------
class ConsejosProfesores(models.Model):
    idConsejo = models.AutoField(primary_key=True, auto_created=True)
    Administrativo = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    FechaHoraRegistroConsejo = models.DateTimeField(blank=True, auto_now_add=True)
    FechaHoraPlanificadaConsejo = models.DateTimeField(blank=True)
    ComentariosConsejo = models.TextField(max_length=100, blank=False)
    AcuerdosConsejo = models.TextField(blank=False)
    Archivo1Consejo = models.FileField(upload_to="images/consejos/",null=True,blank=True)
    Archivo2Consejo = models.FileField(upload_to="images/consejos/",null=True,blank=True)
    Archivo3Consejo = models.FileField(upload_to="images/consejos/",null=True,blank=True)
    NumeroProfesoresConsejo = models.IntegerField(default = 0,blank=False)

    def save(self, *args, **kwargs):

        if not self.Archivo1Consejo:
            self.Archivo1Consejo = 'images/consejos/sinimagen.png'
        if not self.Archivo2Consejo:
            self.Archivo2Consejo = 'images/consejos/sinimagen.png'
        if not self.Archivo3Consejo:
            self.Archivo3Consejo = 'images/consejos/sinimagen.png'

        super(ConsejosProfesores, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.idConsejo} / {self.Administrativo.last_name} {self.Administrativo.first_name}"
#-------------------------------------------------------------------------------------------------
#----------------------------------------Modelo de Impresiones------------------------------------
#-------------------------------------------------------------------------------------------------
class Impresiones(models.Model):
    idImpresion = models.AutoField(primary_key=True, auto_created=True)
    ProfesorImpresion = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    FechaHoraRegistroImpresion = models.DateTimeField(blank=True, auto_now_add=True)
    FechaHoraUtilizacionImpresion = models.DateTimeField(blank=True)
    CursoImpresion = models.CharField(max_length=50, choices=CURSOS_CHOICE,blank=False)
    AsignaturaImpresion = models.CharField(max_length=50, blank=False)
    Archivo1Impresion = models.FileField(upload_to="images/impresiones/",null=True,blank=True)
    Archivo2Impresion = models.FileField(upload_to="images/impresiones/",null=True,blank=True)
    Archivo3Impresion = models.FileField(upload_to="images/impresiones/",null=True,blank=True)
    ObservacionImpresion = models.TextField(blank=False)
    EstadoImpresion = models.CharField(max_length=50, choices=ESTADOIMPRESION_CHOICES,blank=False, default="PENDIENTE")

    def save(self, *args, **kwargs):

        if not self.Archivo1Impresion:
            self.Archivo1Impresion = 'images/impresiones/sinimagen.png'
        if not self.Archivo2Impresion:
            self.Archivo2Impresion = 'images/impresiones/sinimagen.png'
        if not self.Archivo3Impresion:
            self.Archivo3Impresion = 'images/impresiones/sinimagen.png'

        super(Impresiones, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.idImpresion} / {self.ProfesorImpresion.last_name} {self.ProfesorImpresion.first_name}"
#-------------------------------------------------------------------------------------------------