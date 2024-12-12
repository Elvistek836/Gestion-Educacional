from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profesor, DisponibilidadProfesor

@receiver(post_save, sender=Profesor)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        usuario = User.objects.create_user(
            id=instance.id,
            username=instance.rut,
            email=instance.email,
            password="Ingresar01"
        )
        usuario.first_name = instance.nombre
        usuario.last_name = instance.apellido
        usuario.is_staff = True  # Esto permite que el usuario acceda al admin
        usuario.save()

        id=instance.id
        estado="NO DISPONIBLE"
        dia1="LUNES"
        dia2="MARTES"
        dia3="MIERCOLES"
        dia4="JUEVES"
        dia5="VIERNES"
        d=DisponibilidadProfesor(bloque=1,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=2,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=3,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=4,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=5,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=6,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=7,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=8,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=9,dia=dia1,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=1,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=2,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=3,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=4,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=5,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=6,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=7,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=8,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=9,dia=dia2,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=1,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=2,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=3,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=4,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=5,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=6,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=7,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=8,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=9,dia=dia3,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=1,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=2,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=3,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=4,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=5,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=6,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=7,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=8,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=9,dia=dia4,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=1,dia=dia5,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=2,dia=dia5,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=3,dia=dia5,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=4,dia=dia5,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=5,dia=dia5,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=6,dia=dia5,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=7,dia=dia5,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=8,dia=dia5,estado=estado,profesor_id=id)
        d.save()
        d=DisponibilidadProfesor(bloque=9,dia=dia5,estado=estado,profesor_id=id)
        d.save()