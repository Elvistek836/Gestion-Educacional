from datetime import datetime
from django.shortcuts import render
from django.db import connection
from .models import Profesor, Asignatura, Curso, AsignaturasProfesor, DisponibilidadProfesor, Horario, Usuario, Historial

def mostrarIndex(request):
    us=Usuario.objects.all().values()
    cur=Curso.objects.all().values()
    if us:
        if cur:
            usu=Usuario.objects.all().order_by("id")
            datos={"uc":'Cursos y Usuarios cargados correctamente!!',"usu":usu}
            return render(request,'index.html',datos)
        else:
            datos={"c":'Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"u":'Debe cargar los Usuarios y las Cursos'}
        return render(request,'index.html',datos)
#----------------------------------------------------------------------
def registrarUsuarios(request):
    if request.method=="POST":
        nom1="DIRECTORA"
        nom2="SECRETARIA"
        pas1="123456"
        pas2="654321"
        u=Usuario(nombre=nom1,password=pas1)
        u.save()
        us=Usuario(nombre=nom2,password=pas2)
        us.save()
        datos={"r":'Usuarios creados correctamente!!',"c":'Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
    else:
        datos={"r2":'Error al realizar solicitud!!'}
        return render(request,'index.html',datos)
#-----------------------------------------------------------------------
def registrarCursos(request):
    if request.method=="POST":
        nom1="PRIMERO BASICO"
        nom2="SEGUNDO BASICO"
        nom3="TERCERO BASICO"
        nom4="CUARTO BASICO"
        nom5="QUINTO BASICO"
        nom6="SEXTO BASICO"
        nom7="SEPTIMO BASICO"
        nom8="OCTAVO BASICO"
        nom9="PRIMERO MEDIO"                                       #Registra todos los cursos con sus horarios vacios, listos para ser editados
        nom10="SEGUNDO MEDIO"                                      #Desde la Linea 37 hasta la 1074.
        nom11="TERCERO MEDIO"
        nom12="CUARTO MEDIO"
        nom13="KINDER"
        nom14="PRE-KINDER"
        c=Curso(nombre=nom1)
        c.save()
        c=Curso(nombre=nom2)
        c.save()
        c=Curso(nombre=nom3)
        c.save()
        c=Curso(nombre=nom4)
        c.save()
        c=Curso(nombre=nom5)
        c.save()
        c=Curso(nombre=nom6)
        c.save()
        c=Curso(nombre=nom7)
        c.save()
        c=Curso(nombre=nom8)
        c.save()
        c=Curso(nombre=nom9)
        c.save()
        c=Curso(nombre=nom10)
        c.save()
        c=Curso(nombre=nom11)
        c.save()
        c=Curso(nombre=nom12)
        c.save()
        c=Curso(nombre=nom13)
        c.save()
        c=Curso(nombre=nom14)
        c.save()
        c=Curso.objects.get(nombre=nom1)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom2)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()


        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom3)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom4)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom5)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom6)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom7)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom8)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom9)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom10)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom11)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom12)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()

        c=Curso.objects.get(nombre=nom13)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()


        c=Curso.objects.get(nombre=nom14)
        id=c.id
        h=Horario(bloque=1,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="LUNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="LUNES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MARTES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MARTES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="MIERCOLES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="MIERCOLES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="JUEVES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="JUEVES",curso_id=id)
        h.save()

        h=Horario(bloque=1,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=2,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=3,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=4,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=5,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=6,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=7,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=8,dia="VIERNES",curso_id=id)
        h.save()
        h=Horario(bloque=9,dia="VIERNES",curso_id=id)
        h.save()
        datos={"r":'Cursos cargados correctamente!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
    else:
        datos={"r2":'Error al realizar solicitud!!'}
        return render(request,'index.html',datos)
#-----------------------------------------------------------------
def iniciarSesion(request):
    if request.method=="POST":
        nom=request.POST["txtusu"].upper()
        pas=request.POST["txtpas"]
        comprobarLogin=Usuario.objects.filter(nombre=nom,password=pas).values()
        if comprobarLogin:
            request.session["idUsuario"]=comprobarLogin[0]["id"]
            request.session["nomUsuario"]=nom.upper()
            request.session["pasUsuario"]=pas
            datos={'nomUsuario':nom.upper()}
            if nom=="DIRECTORA":
                des="Inicio de Sesion "+str(nom)+""
                tabla=""
                fyh=datetime.now()
                usuario=request.session.get("idUsuario")
                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                his.save()
                return render(request,'menu_directora.html',datos)
            else:
                des="Inicio de Sesion "+str(nom)+""
                tabla=""
                fyh=datetime.now()
                usuario=request.session.get("idUsuario")
                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                his.save()
                datos={"nomUsuario":nom.upper()}
                return render(request,'menu_secretaria.html',datos)
        else:
            datos={"r2":'Error de Usuario y/o contraseña',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe presionar el boton de inicio de sesion',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#------------------------------------------------------------------
def mostrarMenuDirectora(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="DIRECTORA":
            datos={"nomUsuario":nomUsuario}
            return render(request,'menu_directora.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder al menu del usuario Directora!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#------------------------------------------------------------------
def mostrarMenuSecretaria(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            datos={"nomUsuario":nomUsuario}
            return render(request,'menu_secretaria.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder al menu del usuario Secretaria!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-------------------------------------------------------------------
def cerrarSesion(request):
    try:
        nom=request.session.get("nomUsuario")
        des="Cierre de Sesion "+str(nom)+""
        tabla=""
        fyh=datetime.now()
        usuario=request.session.get("idUsuario")
        his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
        his.save()
        del request.session["idUsuario"]
        del request.session["nomUsuario"]
        del request.session["pasUsuario"]
        datos={"r":'Sesion cerrada correctamente',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
    except:
        datos={"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#------------Asignaturas-------------------------------------------------------
def mostrarRegistrarAsig(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
            cur=Curso.objects.all()
            datos={"nomUsuario":nomUsuario,"cur":cur,"asg":asg}
            return render(request,'registrar_asignatura.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder al registro de Asignaturas!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-------------------------------------------------------------------
def mostrarModificarAsig(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            rs=Asignatura.objects.select_related("curso").filter(id=id)
            if rs:
                asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                cur=Curso.objects.all()
                datos={"nomUsuario":nomUsuario,"asg":asg,"rs":rs,"cur":cur}
                return render(request,'modificar_asignatura.html',datos)
            else:
                asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                cur=Curso.objects.all()
                datos={"nomUsuario":nomUsuario,"cur":cur,"asg":asg,"r2":'Asignatura no disponible!!'}
                return render(request,'registrar_asignatura.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder al registro de Asignaturas!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-------------------------------------------------------------------
def registrarAsignatura(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario == "SECRETARIA":
            if request.method=="POST":
                cod=request.POST["txtcod"].upper()
                mat=request.POST["opasg"]
                cur=request.POST["opcur"]
                comprobarAsignatura=Asignatura.objects.filter(codigo=cod.upper())
                cur=int(cur)
                if comprobarAsignatura:
                    asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")                          #Registra las Asignaturas y las evalua para determinar sus bloques semanales
                    cur=Curso.objects.all()                                                                                     #Desde la linea 1191 hasta la 1407
                    datos={"r2":'El codigo ya esta en uso!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                    return render(request,'registrar_asignatura.html',datos)
                else:
                    comprobarAsignatura=Asignatura.objects.filter(nombre=mat,curso_id=cur)
                    if comprobarAsignatura:
                        asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                        cur=Curso.objects.all()
                        datos={"nomUsuario":nomUsuario,"cur":cur,"asg":asg,"r2":'Asignatura ya Registrada para el curso seleccionado!!'}
                        return render(request,'registrar_asignatura.html',datos)
                    else:
                        if (mat=="Biología" or mat=="Química" or mat=="Física" or mat=="Filosofía y Psicología") and cur<=10 or mat=="Tecnología" and cur>=11:
                            asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                            cur=Curso.objects.all()
                            datos={"r2":'La asignatura no corresponde al curso seleccionado!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                            return render(request,'registrar_asignatura.html',datos)
                        else:
                            if cur<=8:
                                niv="BASICA"
                                if cur<=4 and mat=="Idioma Extranjero: Inglés":
                                    asg=Asignatura.objects.select_related("curso").all().order_by("codigo")
                                    cur=Curso.objects.all()
                                    datos={"r2":'La asignatura no corresponde al curso seleccionado!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                                    return render(request,'registrar_asignatura.html',datos)
                                else:
                                    if cur>=1 and cur<=4:
                                        if mat=="Lenguaje y Comunicación (1ero a 4to Basico) - 8hrs":
                                            blo=8
                                        if mat=="Matemática  (1ero Basico a 2do Medio) - 6hrs":
                                            blo=6
                                        if mat=="Historia, Geografía y Ciencias Sociales (1ero a 4to Basico) - 3hrs":
                                            blo=3
                                        if mat=="Artes Visuales (1ero a 4to Basico) - 2hrs":
                                            blo=2
                                        if mat=="Música  (1ero a 4to Basico) - 2hrs":
                                            blo=2
                                        if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                            blo=2
                                        if mat=="Orientación  (1ero a 4to Basico) - 1hr":
                                            blo=1
                                        if mat=="Tecnología  (1ero a 4to Basico) - 1hr":
                                            blo=1
                                        if mat=="Religión (Todas) - 2hrs":
                                            blo=2
                                        if mat=="Ciencias Naturales (1ero a 6to Basico) - 3hrs":
                                            blo=3
                                        if mat=="Inglés (Libre Disposicion)  (1ero a 4to Basico) - 1hr":
                                            blo=1
                                    if cur==5 or cur==6:
                                        if mat=="Lenguaje y Comunicación  (5to y 6to Basico) - 6hrs":
                                            blo=6
                                        if mat=="Matemática  (1ero Basico a 2do Medio) - 6hrs":
                                            blo=6
                                        if mat=="Historia, Geografía y Ciencias Sociales  (5to a 2do Medio) - 4hrs":
                                            blo=4
                                        if mat=="Artes Visuales (5to a 6to Basico) - 1hr":
                                            blo=1
                                        if mat=="Música  (5to y 6to Basico) - 1hr":
                                            blo=1
                                        if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                            blo=2
                                        if mat=="Orientación  (5to a 2do Medio) - 1hr":
                                            blo=1
                                        if mat=="Tecnología  (5to a 2do Medio) - 1hr":
                                            blo=1
                                        if mat=="Religión (Todas) - 2hrs":
                                            blo=2
                                        if mat=="Ciencias Naturales (1ero a 6to Basico) - 3hrs":
                                            blo=3
                                        if mat=="Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs":
                                            blo=3
                                    if cur==7 or cur==8:
                                        if mat=="Lengua y Literatura (7mo a 2do Medio) - 6hrs":
                                            blo=6
                                        if mat=="Matemática  (1ero Basico a 2do Medio) - 6hrs":
                                            blo=6
                                        if mat=="Historia, Geografía y Ciencias Sociales  (5to a 2do Medio) - 4hrs":
                                            blo=4
                                        if mat=="Artes Visuales y Música (7mo y 8vo Basico) - 2hrs":
                                            blo=2
                                        if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                            blo=2
                                        if mat=="Orientación  (5to a 2do Medio) - 1hr":
                                            blo=1
                                        if mat=="Tecnología  (5to a 2do Medio) - 1hr":
                                            blo=1
                                        if mat=="Religión (Todas) - 2hrs":
                                            blo=2
                                        if mat=="Ciencias Naturales  (7mo y 8vo Basico) - 4hrs":
                                            blo=4
                                        if mat=="Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs":
                                            blo=3
                                    a=Asignatura(codigo=cod.upper(),nombre=mat,nivel=niv,bloques=blo,curso_id=cur)
                                    a.save()
                                    des="Registro de Asignatura "+str(cod)+""
                                    tabla="Asignatura"
                                    fyh=datetime.now()
                                    usuario=request.session.get("idUsuario")
                                    his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                    his.save()
                                    asg=Asignatura.objects.select_related("curso").all().order_by("codigo")
                                    cur=Curso.objects.all()
                                    datos={"r":'La asignatura se registro con exito',"asg":asg,"cur":cur,"nomUsuario":nomUsuario}
                                    return render(request,'registrar_asignatura.html',datos)
                            elif cur==13 or cur==14:
                                niv="PREBASICA"
                                if cur==13:
                                    if mat=="Religión (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Inglés Nivel Transicion (Prekinder y Kinder) - 1hr":
                                        blo=1
                                    if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Asignatura Kinder - 1hr":
                                        blo=1
                                else:
                                    if mat=="Asignatura PreKinder - 1hr":
                                        blo=1
                                    if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Inglés Nivel Transicion (Prekinder y Kinder) - 1hr":
                                        blo=1
                                    if mat=="Religión (Todas) - 2hrs":
                                        blo=2
                                a=Asignatura(codigo=cod.upper(),nombre=mat,nivel=niv,bloques=blo,curso_id=cur)
                                a.save()
                                des="Registro de Asignatura "+str(cod)+""
                                tabla="Asignatura"
                                fyh=datetime.now()
                                usuario=request.session.get("idUsuario")
                                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                his.save()
                                asg=Asignatura.objects.select_related("curso").all().order_by("codigo")
                                cur=Curso.objects.all()
                                datos={"r":'La asignatura se registro con exito',"asg":asg,"cur":cur,"nomUsuario":nomUsuario}
                                return render(request,'registrar_asignatura.html',datos)
                            else:
                                niv="MEDIA"
                                if cur==9 or cur==10:
                                    if mat=="Lengua y Literatura (7mo a 2do Medio) - 6hrs":
                                        blo=6
                                    if mat=="Matemática  (1ero Basico a 2do Medio) - 6hrs":
                                        blo=6
                                    if mat=="Historia, Geografía y Ciencias Sociales  (5to a 2do Medio) - 4hrs":
                                        blo=4
                                    if mat=="Artes Visuales o Música (1ero y 2do Medio) - 2hrs":
                                        blo=2
                                    if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Orientación  (5to a 2do Medio) - 1hr":
                                        blo=1
                                    if mat=="Tecnología  (5to a 2do Medio) - 1hr":
                                        blo=1
                                    if mat=="Religión (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs":
                                        blo=3
                                    if mat=="Ciencias Naturales  (1ero y 2do Medio) - 6hrs":
                                        blo=6
                                if cur==11 or cur==12:
                                    if mat=="Lengua y Literatura (3ero y 4to Medio) - 3hrs":
                                        blo=3
                                    if mat=="Matemática  (3ero y 4to Medio) - 3hrs":
                                        blo=3
                                    if mat=="Historia, Geografía y Ciencias Sociales (3ero y 4to Medio) - 2hrs":
                                        blo=2
                                    if mat=="Artes (3ero y 4to Medio) - 2hrs":
                                        blo=2
                                    if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Ciencias para la Ciudadanía (3ero y 4to Medio) - 2hrs":
                                        blo=2
                                    if mat=="Religión (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Inglés (3ero y 4to Medio) - 2hrs":
                                        blo=2
                                    if mat=="Filosofía (3ero y 4to Medio) - 2hrs":
                                        blo=2
                                    if mat=="Electivo de lengua y literatura (3ero y 4to Medio) - 6hrs":
                                        blo=6
                                    if mat=="Electivo de historia (3ero y 4to Medio) - 6hrs":
                                        blo=6
                                    if mat=="Electivo de matematicas (3ero y 4to Medio) - 6hrs":
                                        blo=6
                                    if mat=="Electivo de biología (3ero y 4to Medio) - 6hrs":
                                        blo=6
                                    if mat=="Educación Ciudadana (3ero y 4to Medio) - 2hrs":
                                        blo=2
                                    if mat=="Ciencias para la Ciudadanía (3ero y 4to Medio) - 2hrs":
                                        blo=2
                                a=Asignatura(codigo=cod.upper(),nombre=mat,nivel=niv,bloques=blo,curso_id=cur)
                                a.save()
                                des="Registro de Asignatura "+str(cod)+""
                                tabla="Asignatura"
                                fyh=datetime.now()
                                usuario=request.session.get("idUsuario")
                                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                his.save()
                                cur=Curso.objects.all()
                                asg=Asignatura.objects.select_related("curso").all().order_by("codigo")
                                datos={"r":'La asignatura se registro con exito',"asg":asg,"nomUsuario":nomUsuario,"cur":cur}
                                return render(request,'registrar_asignatura.html',datos)
            else:
                asg=Asignatura.objects.select_related("curso").all().order_by("codigo")
                cur=Curso.objects.all()
                datos={"nomUsuario":nomUsuario,"cur":cur,"asg":asg,"r2":'Debe presionar el boton para registrar!!'}
                return render(request,'registrar_asignatura.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder al registro de Asignatura!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-----------------------------------------------------------------------------------
def eliminarAsignatura(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario =="SECRETARIA":
            asg=Asignatura.objects.filter(id=id)
            if asg:
                ag=Asignatura.objects.get(id=id)
                cod=ag.codigo
                h=Horario.objects.filter(asignatura_id=id)
                if h:
                    j=0
                    for x in h:
                        if x == h[j]:
                            y=Horario.objects.get(id=h[j].id)
                            y.profesor_id=""
                            y.asignatura_id=""
                            y.save()
                        j=j+1
                asg.delete()
                des="Eliminacion de Asignatura "+str(cod)+""
                tabla="Asignatura"
                fyh=datetime.now()
                usuario=request.session.get("idUsuario")
                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                his.save()
                asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                cur=Curso.objects.all()
                datos={"r":'Asignatura eliminada Correctamente!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                return render(request,'registrar_asignatura.html',datos)
            else:
                asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                cur=Curso.objects.all()
                datos={"r2":'la Asignatura no se pudo eliminar!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                return render(request,'registrar_asignatura.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-----------------------------------------------------------------------------------
def modificarAsignatura(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            if request.method=="POST":
                cod=request.POST["txtcod"].upper()
                mat=request.POST["opasg"]
                cur=request.POST["opcur"]
                comprobarCodigo=Asignatura.objects.filter(codigo=cod.upper())
                cur=int(cur)
                if comprobarCodigo:
                    comprobarA=Asignatura.objects.filter(id=id,codigo=cod.upper())
                    if comprobarA:
                        a=Asignatura.objects.get(id=id)

                    else:
                        asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                        cur=Curso.objects.all()
                        datos={"r2":'Codigo ya en uso!!',"asg":asg,"cur":cur,"nomUsuario":nomUsuario}
                        return render(request,'modificar_asignatura.html',datos)
                else:
                    a=Asignatura.objects.get(id=id)
                    a.codigo=cod.upper()
                    if (mat=="Biología" or mat=="Química" or mat=="Física" or mat=="Filosofía y Psicología") and cur<=10 or mat=="Tecnología" and cur>=11:
                            asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                            cur=Curso.objects.all()
                            datos={"r2":'La asignatura no corresponde al curso seleccionado!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                            return render(request,'registrar_asignatura.html',datos)
                    else:
                        if cur<=8:
                            niv="BASICA"
                            if cur<=4 and mat=="Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs":
                                asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                                cur=Curso.objects.all()
                                datos={"r2":'La asignatura no corresponde al curso seleccionado!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                                return render(request,'registrar_asignatura.html',datos)
                            else:
                                if cur>=1 and cur<=4:
                                    if mat=="Lenguaje y Comunicación (1ero a 4to Basico) - 8hrs":
                                        blo=8
                                    if mat=="Matemática  (1ero Basico a 2do Medio) - 6hrs":
                                        blo=6
                                    if mat=="Historia, Geografía y Ciencias Sociales (1ero a 4to Basico) - 3hrs":
                                        blo=3
                                    if mat=="Artes Visuales (1ero a 4to Basico) - 2hrs":
                                        blo=2
                                    if mat=="Música  (1ero a 4to Basico) - 2hrs":
                                        blo=2
                                    if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Orientación  (1ero a 4to Basico) - 1hr":
                                        blo=1
                                    if mat=="Tecnología  (1ero a 4to Basico) - 1hr":
                                        blo=1
                                    if mat=="Religión (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Ciencias Naturales (1ero a 6to Basico) - 3hrs":
                                        blo=3
                                    if mat=="Inglés (Libre Disposicion)  (1ero a 4to Basico) - 1hr":
                                        blo=1
                                if cur==5 or cur==6:
                                    if mat=="Lenguaje y Comunicación  (5to y 6to Basico) - 6hrs":
                                        blo=6
                                    if mat=="Matemática  (1ero Basico a 2do Medio) - 6hrs":
                                        blo=6
                                    if mat=="Historia, Geografía y Ciencias Sociales  (5to a 2do Medio) - 4hrs":
                                        blo=4
                                    if mat=="Artes Visuales (5to a 6to Basico) - 1hr":
                                        blo=1
                                    if mat=="Música  (5to y 6to Basico) - 1hr":
                                        blo=1
                                    if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Orientación  (5to a 2do Medio) - 1hr":
                                        blo=1
                                    if mat=="Tecnología  (5to a 2do Medio) - 1hr":
                                        blo=1
                                    if mat=="Religión (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Ciencias Naturales (1ero a 6to Basico) - 3hrs":
                                        blo=3
                                    if mat=="Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs":
                                        blo=3
                                if cur==7 or cur==8:
                                    if mat=="Lengua y Literatura (7mo a 2do Medio) - 6hrs":
                                        blo=6
                                    if mat=="Matemática  (1ero Basico a 2do Medio) - 6hrs":
                                        blo=6
                                    if mat=="Historia, Geografía y Ciencias Sociales  (5to a 2do Medio) - 4hrs":
                                        blo=4
                                    if mat=="Artes Visuales y Música (7mo y 8vo Basico) - 2hrs":
                                        blo=2
                                    if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Orientación  (5to a 2do Medio) - 1hr":
                                        blo=1
                                    if mat=="Tecnología  (5to a 2do Medio) - 1hr":
                                        blo=1
                                    if mat=="Religión (Todas) - 2hrs":
                                        blo=2
                                    if mat=="Ciencias Naturales  (7mo y 8vo Basico) - 4hrs":
                                        blo=4
                                    if mat=="Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs":
                                        blo=3
                                h=Horario.objects.filter(asignatura_id=id)
                                if h:
                                    j=0
                                    for x in h:
                                        if x == h[j]:
                                            y=Horario.objects.get(id=h[j].id)
                                            y.profesor_id=""
                                            y.asignatura_id=""
                                            y.save()

                                        j=j+1

                                cur=str(cur)
                                a.nombre=mat
                                a.nivel=niv
                                a.bloque=blo
                                a.curso_id=cur
                                a.save()
                                h=Horario.objects.filter(asignatura_id=id)

                                des="Modificacion de Asignatura "+str(cod)+""
                                tabla="Asignatura"
                                fyh=datetime.now()
                                usuario=request.session.get("idUsuario")
                                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                his.save()
                                asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                                cur=Curso.objects.all()
                                datos={"r":'Asignatura modificada Correctamente!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                                return render(request,'registrar_asignatura.html',datos)
                        elif cur==13 or cur==14:
                            niv="PREBASICA"
                            if cur==13:
                                if mat=="Religión (Todas) - 2hrs":
                                    blo=2
                                if mat=="Inglés Nivel Transicion (Prekinder y Kinder) - 1hr":
                                    blo=1
                                if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                    blo=2
                                if mat=="Asignatura Kinder - 1hr":
                                    blo=1
                            else:
                                if mat=="Asignatura PreKinder - 1hr":
                                    blo=1
                                if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                    blo=2
                                if mat=="Inglés Nivel Transicion (Prekinder y Kinder) - 1hr":
                                    blo=1
                                if mat=="Religión (Todas) - 2hrs":
                                    blo=2
                            cur=str(cur)
                            a.nombre=mat
                            a.nivel=niv
                            a.bloque=blo
                            a.curso_id=cur
                            a.save()
                            h=Horario.objects.filter(asignatura_id=id)

                            des="Modificacion de Asignatura "+str(cod)+""
                            tabla="Asignatura"
                            fyh=datetime.now()
                            usuario=request.session.get("idUsuario")
                            his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                            his.save()
                            asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                            cur=Curso.objects.all()
                            datos={"r":'Asignatura modificada Correctamente!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                            return render(request,'registrar_asignatura.html',datos)        
                        else:
                            niv="MEDIA"
                            if cur==9 or cur==10:
                                if mat=="Lengua y Literatura (7mo a 2do Medio) - 6hrs":
                                    blo=6
                                if mat=="Matemática  (1ero Basico a 2do Medio) - 6hrs":
                                    blo=6
                                if mat=="Historia, Geografía y Ciencias Sociales  (5to a 2do Medio) - 4hrs":
                                    blo=4
                                if mat=="Artes Visuales o Música (1ero y 2do Medio) - 2hrs":
                                    blo=2
                                if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                    blo=2
                                if mat=="Orientación  (5to a 2do Medio) - 1hr":
                                    blo=1
                                if mat=="Tecnología  (5to a 2do Medio) - 1hr":
                                    blo=1
                                if mat=="Religión (Todas) - 2hrs":
                                    blo=2
                                if mat=="Idioma Extranjero: Inglés  (5to a 2do medio) - 3hrs":
                                    blo=3
                                if mat=="Ciencias Naturales  (1ero y 2do Medio) - 6hrs":
                                    blo=6
                            if cur==11 or cur==12:
                                if mat=="Lengua y Literatura (3ero y 4to Medio) - 3hrs":
                                    blo=3
                                if mat=="Matemática  (3ero y 4to Medio) - 3hrs":
                                    blo=3
                                if mat=="Historia, Geografía y Ciencias Sociales (3ero y 4to Medio) - 2hrs":
                                    blo=2
                                if mat=="Artes (3ero y 4to Medio) - 2hrs":
                                    blo=2
                                if mat=="Educación Física y Salud  (Todas) - 2hrs":
                                    blo=2
                                if mat=="Ciencias para la Ciudadanía (3ero y 4to Medio) - 2hrs":
                                    blo=2
                                if mat=="Religión (Todas) - 2hrs":
                                    blo=2
                                if mat=="Inglés (3ero y 4to Medio) - 2hrs":
                                    blo=2
                                if mat=="Filosofía (3ero y 4to Medio) - 2hrs":
                                    blo=2
                                if mat=="Electivo de lengua y literatura (3ero y 4to Medio) - 6hrs":
                                    blo=6
                                if mat=="Electivo de historia (3ero y 4to Medio) - 6hrs":
                                    blo=6
                                if mat=="Electivo de matematicas (3ero y 4to Medio) - 6hrs":
                                    blo=6
                                if mat=="Electivo de biología (3ero y 4to Medio) - 6hrs":
                                    blo=6
                                if mat=="Educación Ciudadana (3ero y 4to Medio) - 2hrs":
                                    blo=2
                                if mat=="Ciencias para la Ciudadanía (3ero y 4to Medio) - 2hrs":
                                    blo=2
                            h=Horario.objects.filter(asignatura_id=id)
                            if h:
                                j=0
                                for x in h:
                                    if x == h[j]:
                                        y=Horario.objects.get(id=h[j].id)
                                        y.profesor_id=""
                                        y.asignatura_id=""
                                        y.save()
                                    j=j+1

                            cur=str(cur)
                            a.nombre=mat
                            a.nivel=niv
                            a.bloque=blo
                            a.curso_id=cur
                            a.save()

                            des="Modificacion de Asignatura "+str(cod)+""
                            tabla="Asignatura"
                            fyh=datetime.now()
                            usuario=request.session.get("idUsuario")
                            his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                            his.save()
                            asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                            cur=Curso.objects.all()
                            datos={"r":'Asignatura modificada Correctamente!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                            return render(request,'registrar_asignatura.html',datos)
            else:
                asg=Asignatura.objects.select_related("curso").all().order_by("curso_id")
                cur=Curso.objects.all()
                datos={"r2":'Error al realizar la modificacion!!',"cur":cur,"asg":asg,"nomUsuario":nomUsuario}
                return render(request,'registrar_asignatura.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#--------------Profesores--------------------------------------------------------
def mostrarRegistrarPro(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            pro=Profesor.objects.all().values().order_by("rut")
            datos={"nomUsuario":nomUsuario,"pro":pro}
            return render(request,'registrar_profesor.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-------------------------------------------------------------------------
def mostrarModificarPro(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            rs=Profesor.objects.filter(id=id)
            if rs:
                pro=Profesor.objects.all().values().order_by("rut")
                datos={"nomUsuario":nomUsuario,"pro":pro,"rs":rs}
                return render(request,'modificar_profesor.html',datos)
            else:
                pro=Profesor.objects.all().values().order_by("rut")
                datos={"nomUsuario":nomUsuario,"pro":pro,"r2":'Profesor no disponible!!'}
                return render(request,'registrar_profesor.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#---------------------------------------------------------------------------
def registrarProfesor(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            if request.method=="POST":
                rut=request.POST["txtrut"]
                nom=request.POST["txtnom"]
                ape=request.POST["txtape"]
                niv=request.POST["opniv"]
                comprobarProfesor=Profesor.objects.filter(rut=rut)
                if comprobarProfesor:
                    pro=Profesor.objects.all().values().order_by("rut")
                    datos={"r2":'Profesor ya registrado',"pro":pro,"nomUsuario":nomUsuario}
                    return render(request,'registrar_profesor.html',datos)
                else:
                    p=Profesor(rut=rut,nombre=nom,apellido=ape,nivel=niv)
                    p.save()
                    des="Registro de Profesor "+str(rut)+""
                    tabla="Profesor"
                    fyh=datetime.now()
                    usuario=request.session.get("idUsuario")
                    his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                    his.save()
                    pr=Profesor.objects.get(rut=rut)
                    id=pr.id
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
                    pro=Profesor.objects.all().values().order_by("rut")
                    datos={"r":'Profesor registrado correctamente',"pro":pro,"nomUsuario":nomUsuario}
                    return render(request,'registrar_profesor.html',datos)
            else:
                pro=Profesor.objects.all().values().order_by("rut")
                datos={"r2":'No se pudo ejecutar la solicitud',"pro":pro,"nomUsuario":nomUsuario}
                return render(request,'registrar_profesor.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-------------------------------------------------------------------------------
def modificarProfesor(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            if request.method=="POST":
                rut=request.POST["txtrut"]
                nom=request.POST["txtnom"]
                ape=request.POST["txtape"]
                niv=request.POST["opniv"]
                comprobarRut=Profesor.objects.filter(rut=rut)
                if comprobarRut:
                    RutID=Profesor.objects.filter(id=id,rut=rut)
                    if RutID:
                        p=Profesor.objects.get(id=id)
                        if p.nivel==niv:
                            p=Profesor.objects.get(id=id)
                            p.nombre=nom
                            p.apellido=ape
                            p.save()
                        else:
                            p=Profesor.objects.get(id=id)
                            p.nombre=nom
                            p.apellido=ape
                            p.nivel=niv
                            p.save()

                            h=Horario.objects.filter(profesor_id=id)
                            if h:
                                j=0
                                for x in h:
                                    if x == h[j]:
                                        y=Horario.objects.get(id=h[j].id)
                                        y.profesor_id=""
                                        y.asignatura_id=""
                                        y.save()

                                    j=j+1

                        des="Modificacion de Profesor "+str(rut)+""
                        tabla="Profesor"
                        fyh=datetime.now()
                        usuario=request.session.get("idUsuario")
                        his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                        his.save()
                        pro=Profesor.objects.all().values().order_by("rut")
                        datos={"r":'Datos Modificados correctamente!!',"pro":pro,"nomUsuario":nomUsuario}
                        return render(request,'registrar_profesor.html',datos)
                    else:
                        pro=Profesor.objects.all().values().order_by("rut")
                        datos={"r2":'El rut indicado ya esta en uso!!',"pro":pro,"nomUsuario":nomUsuario}
                        return render(request,'modificar_profesor.html',datos)
                else:
                    p=Profesor.objects.get(id=id)
                    if p.nivel==niv:
                        p=Profesor.objects.get(id=id)
                        p.rut=rut
                        p.nombre=nom
                        p.apellido=ape
                        p.save()
                    else:
                        p=Profesor.objects.get(id=id)
                        p.rut=rut
                        p.nombre=nom
                        p.apellido=ape
                        p.nivel=niv
                        p.save()
                        h=Horario.objects.filter(profesor_id=id)
                        if h:
                            j=0
                            for x in h:
                                if x == h[j]:
                                    y=Horario.objects.get(id=h[j].id)
                                    y.profesor_id=""
                                    y.asignatura_id=""
                                    y.save()

                                j=j+1

                    des="Modificacion de Profesor "+str(rut)+""
                    tabla="Profesor"
                    fyh=datetime.now()
                    usuario=request.session.get("idUsuario")
                    his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                    his.save()
                    pro=Profesor.objects.all().values().order_by("rut")
                    datos={"r":'Datos Modificados correctamente',"pro":pro,"nomUsuario":nomUsuario}
                    return render(request,'registrar_profesor.html',datos)
            else:
                pro=Profesor.objects.all().values().order_by("rut")
                datos={"r2":'Error al realizar la consulta!!',"pro":pro,"nomUsuario":nomUsuario}
                return render(request,'registrar_profesor.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#---------------------------------------------------------------------------
def eliminarProfesor(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            pro=Profesor.objects.filter(id=id)
            if pro:
                p=Profesor.objects.get(id=id)
                rut=p.rut

                h=Horario.objects.filter(profesor_id=id)
                if h:
                    j=0
                    for x in h:
                        if x == h[j]:
                            y=Horario.objects.get(id=h[j].id)
                            y.profesor_id=""                                                                                  #Eliminacion de Profesores
                            y.asignatura_id=""                                                                                #Metodo para no eliminar datos de tablas que se desean conservar
                            y.save()

                        j=j+1

                pro.delete()
                des="Eliminacion de Profesor "+str(rut)+""
                tabla="Profesor"
                fyh=datetime.now()
                usuario=request.session.get("idUsuario")
                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                his.save()
                pro=Profesor.objects.all().values().order_by("rut")
                datos={"r":'Profesor eliminado Correctamente!!',"pro":pro,"nomUsuario":nomUsuario}
                return render(request,'registrar_profesor.html',datos)
            else:
                pro=Profesor.objects.all().values().order_by("rut")
                datos={"r2":'El Profesor no se pudo eliminar!!',"pro":pro,"nomUsuario":nomUsuario}
                return render(request,'registrar_profesor.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#----------------Horarios----------------------------------------------------------------
def mostrarRegistrarHor(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
            dis=DisponibilidadProfesor.objects.all().values()
            cur=Curso.objects.all().order_by("id")
            pro=Profesor.objects.all().order_by("rut")
            hor=Horario.objects.select_related("curso","asignatura","profesor").all().order_by("curso_id","dia")
            datos={"nomUsuario":nomUsuario,"cur":cur,"asg":asg,"pro":pro,"hor":hor,"dis":dis}
            return render(request,'registrar_horarios.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#---------------------------------------------------------------------------------------
def mostrarHorario(request,id,idc):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
            asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
            hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=idc)
            hor2=Horario.objects.all().values()
            asgpro=AsignaturasProfesor.objects.select_related("asignartura","profesor")

            query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"
            #print("Consulta SQL:", query)

            with connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()

            query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
            with connection.cursor() as cursor:
                cursor.execute(query)
                results2 = cursor.fetchall()

            datos = {"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "idc":idc, "hor2":hor2, "asgpro":asgpro}

            return render(request, 'modificar_horario.html', datos)

        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#---------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
def cambiarHorario(request,id, idc):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario == "SECRETARIA":
            if request.method=="POST":
                if 'btnguardar' in request.POST:
                        h=Horario.objects.get(id=id)
                        asi=request.POST["opasg"]
                        pr=request.POST["oppro"]
                        dia=h.dia
                        bl=h.bloque
                        id2=h.curso_id
                        rp=h.profesor_id
                        id2=int(id2)
                        comprobarDis=DisponibilidadProfesor.objects.filter(profesor_id=pr,dia=dia,bloque=bl,estado="DISPONIBLE")
                        if comprobarDis:
                            asgi=Asignatura.objects.get(id=asi)
                            blo=asgi.bloques                                                         #Modificacion y/o Registro de Horarios
                            nv=asgi.nivel
                            nom=asgi.nombre
                            comprobarAsi=Horario.objects.filter(asignatura_id=asi,curso_id=id2)
                            if len(comprobarAsi)==blo:
                                j=0
                                for i in comprobarAsi:
                                    if id == comprobarAsi[j].id:
                                        comprobarEsp=AsignaturasProfesor.objects.filter(nombre=nom,nivel=nv,profesor_id=pr)
                                        if comprobarEsp:
                                            ho=Horario.objects.filter(profesor_id=pr,bloque=bl,dia=dia)
                                            if ho:
                                                ho=Horario.objects.get(profesor_id=pr,bloque=bl,dia=dia)
                                                if ho.curso_id == id2:
                                                    h=Horario.objects.get(id=id)
                                                    h.profesor_id=pr
                                                    h.save()

                                                    c=Curso.objects.get(id=id2)
                                                    cu=c.nombre
                                                    des="Modificacion de Horario "+str(cu)+""
                                                    tabla="Horario"
                                                    fyh=datetime.now()
                                                    usuario=request.session.get("idUsuario")
                                                    his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                                    his.save()

                                                    pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
                                                    asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                                    hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                                    hor2=Horario.objects.all().values()

                                                    query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                                    with connection.cursor() as cursor:
                                                        cursor.execute(query)
                                                        results = cursor.fetchall()



                                                    query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                                    with connection.cursor() as cursor:
                                                        cursor.execute(query)
                                                        results2 = cursor.fetchall()

                                                    datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2, "results": results, "results2": results2, "r":'Horario Modificado Correctamente!!',"idc":idc, "hor2":hor2}
                                                    return render(request,'modificar_horario.html',datos)
                                                else:
                                                    pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
                                                    asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                                    hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                                    hor2=Horario.objects.all().values()

                                                    query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                                    with connection.cursor() as cursor:
                                                        cursor.execute(query)
                                                        results = cursor.fetchall()

                                                    query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                                    with connection.cursor() as cursor:
                                                        cursor.execute(query)
                                                        results2 = cursor.fetchall()


                                                    datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2, "results": results,"results2": results2,"r2":'Profesor ya tomo una clase en el bloque seleccionado!!',"idc":idc, "hor2":hor2}
                                                    return render(request,'modificar_horario.html',datos)
                                            else:
                                                h=Horario.objects.get(id=id)
                                                h.profesor_id=pr
                                                h.save()

                                                c=Curso.objects.get(id=id2)
                                                cu=c.nombre
                                                des="Modificacion de Horario "+str(cu)+""
                                                tabla="Horario"
                                                fyh=datetime.now()
                                                usuario=request.session.get("idUsuario")
                                                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                                his.save()

                                                pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
                                                asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                                hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                                hor2=Horario.objects.all().values()

                                                query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                                with connection.cursor() as cursor:
                                                    cursor.execute(query)
                                                    results = cursor.fetchall()


                                                query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                                with connection.cursor() as cursor:
                                                    cursor.execute(query)
                                                    results2 = cursor.fetchall()


                                                datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results,"results2": results2, "r":'Horario Modificado Correctamente!!',"idc":idc, "hor2":hor2}

                                                return render(request,'modificar_horario.html',datos)
                                    j=j+1

                                pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
                                asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                hor2=Horario.objects.all().values()

                                query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                with connection.cursor() as cursor:
                                    cursor.execute(query)
                                    results = cursor.fetchall()


                                query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                with connection.cursor() as cursor:
                                    cursor.execute(query)
                                    results2 = cursor.fetchall()



                                datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2,"r2":'No se puede agregar mas bloques de esta Asignatura en el Curso Seleccionado!!',"idc":idc, "hor2":hor2}
                                return render(request,'modificar_horario.html',datos)
                            else:
                                comprobarEsp=AsignaturasProfesor.objects.filter(nombre=nom,profesor_id=pr)
                                if comprobarEsp:
                                    ho=Horario.objects.filter(profesor_id=pr,bloque=bl,dia=dia)
                                    if ho:
                                        hor=Horario.objects.get(profesor_id=pr,bloque=bl,dia=dia)
                                        if hor.curso_id == id2:
                                            c=Curso.objects.get(id=id2)
                                            cu=c.nombre
                                            h=Horario.objects.get(id=id)
                                            h.asignatura_id=asi
                                            h.profesor_id=pr
                                            h.save()
                                            des="Modificacion de Horario "+str(cu)+""
                                            tabla="Horario"
                                            fyh=datetime.now()
                                            usuario=request.session.get("idUsuario")
                                            his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                            his.save()

                                            pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
                                            asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                            hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                            hor2=Horario.objects.all().values()

                                            query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                            with connection.cursor() as cursor:
                                                cursor.execute(query)
                                                results = cursor.fetchall()


                                            query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                            with connection.cursor() as cursor:
                                                cursor.execute(query)
                                                results2 = cursor.fetchall()



                                            datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "r":'Horario Modificado Correctamente!!',"idc":idc, "hor2":hor2}

                                            return render(request,'modificar_horario.html',datos)
                                        else:
                                            p=0
                                            hor=Horario.objects.filter(profesor_id=pr,bloque=bl,dia=dia)
                                            for x in hor:
                                                p=p+1
                                            if p==1:
                                                c=Curso.objects.get(id=id2)
                                                cu=c.nombre
                                                h=Horario.objects.get(id=id)
                                                h.asignatura_id=asi
                                                h.profesor_id=pr
                                                h.save()
                                                des="Modificacion de Horario "+str(cu)+""
                                                tabla="Horario"
                                                fyh=datetime.now()
                                                usuario=request.session.get("idUsuario")
                                                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                                his.save()

                                                pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")

                                                asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                                hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                                hor2=Horario.objects.all().values()

                                                query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                                with connection.cursor() as cursor:
                                                    cursor.execute(query)
                                                    results = cursor.fetchall()


                                                query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                                with connection.cursor() as cursor:
                                                    cursor.execute(query)
                                                    results2 = cursor.fetchall()



                                                datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "r":'Horario Modificado Correctamente!!',"idc":idc, "hor2":hor2}
                                                return render(request,'modificar_horario.html',datos)
                                            else:
                                                if id2==1 or id2==2 or id2==3 or id2==4 or id2==5 or id2==6 or id2==7 or id2==8:
                                                    pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
                                                else:
                                                    pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
                                                asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                                hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                                hor2=Horario.objects.all().values()

                                                query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                                with connection.cursor() as cursor:
                                                    cursor.execute(query)
                                                    results = cursor.fetchall()

                                                query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                                with connection.cursor() as cursor:
                                                    cursor.execute(query)
                                                    results2 = cursor.fetchall()




                                                datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "r2":'Profesor ya tomo una clase en el bloque seleccionado!!',"idc":idc, "hor2":hor2}
                                                return render(request,'modificar_horario.html',datos)
                                    else:
                                        c=Curso.objects.get(id=id2)
                                        cu=c.nombre
                                        h=Horario.objects.get(id=id)
                                        h.asignatura_id=asi
                                        h.profesor_id=pr
                                        h.save()
                                        des="Modificacion de Horario "+str(cu)+""
                                        tabla="Horario"
                                        fyh=datetime.now()
                                        usuario=request.session.get("idUsuario")
                                        his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                                        his.save()

                                        pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")

                                        asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                        hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                        hor2=Horario.objects.all().values()

                                        query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                        with connection.cursor() as cursor:
                                            cursor.execute(query)
                                            results = cursor.fetchall()


                                        query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                        with connection.cursor() as cursor:
                                            cursor.execute(query)
                                            results2 = cursor.fetchall()



                                        datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "r":'Horario Modificado Correctamente!!',"idc":idc, "hor2":hor2}
                                        return render(request,'modificar_horario.html',datos)
                                else:
                                    pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")

                                    asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                                    hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                                    hor2=Horario.objects.all().values()

                                    query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                                    with connection.cursor() as cursor:
                                        cursor.execute(query)
                                        results = cursor.fetchall()

                                    query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                                    with connection.cursor() as cursor:
                                            cursor.execute(query)
                                            results2 = cursor.fetchall()



                                    datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "r2":'Profesor no capacitado para dictar la Asignatura Seleccionada!!',"idc":idc, "hor2":hor2}
                                    return render(request,'modificar_horario.html',datos)
                        else:
                            pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")

                            asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                            hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                            hor2=Horario.objects.all().values()

                            query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                            with connection.cursor() as cursor:
                                cursor.execute(query)
                                results = cursor.fetchall()

                            query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                            with connection.cursor() as cursor:
                                    cursor.execute(query)
                                    results2 = cursor.fetchall()




                            datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "r2":'Profesor no Disponible para dar clase en este Bloque!!',"idc":idc, "hor2":hor2}
                            return render(request,'modificar_horario.html',datos)


                if 'btnquitar' in request.POST:

                    h=Horario.objects.get(id=id)
                    h.asignatura_id=None
                    h.profesor_id=None
                    h.save()
                    #des="Modificacion de Horario "+str(cu)+""
                    #tabla="Horario"
                    #fyh=datetime.now()
                    #usuario=request.session.get("idUsuario")
                    #his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                    #his.save()

                    pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")
                    asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                    hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=idc)
                    hor2=Horario.objects.all().values()

                    query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                    with connection.cursor() as cursor:
                        cursor.execute(query)
                        results = cursor.fetchall()

                    query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                    with connection.cursor() as cursor:
                            cursor.execute(query)
                            results2 = cursor.fetchall()




                    datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "r":'Horario Quitado Correctamente!!',"idc":idc, "hor2":hor2}
                    return render(request,'modificar_horario.html',datos)





            else:
                h=Horario.objects.get(id=id)
                id2=h.curso_id
                pro2=DisponibilidadProfesor.objects.select_related("profesor").filter(estado="DISPONIBLE").order_by("profesor__nombre")

                asg=Asignatura.objects.select_related("curso").all().order_by("nombre")
                hor=Horario.objects.select_related("curso","asignatura","profesor").filter(curso_id=id2)
                hor2=Horario.objects.all().values()

                query = "select * from horarios_profesor,horarios_asignatura,horarios_asignaturasprofesor where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.nombre=horarios_asignaturasprofesor.nombre and horarios_asignaturasprofesor.profesor_id=horarios_profesor.id group by horarios_profesor.apellido"

                with connection.cursor() as cursor:
                    cursor.execute(query)
                    results = cursor.fetchall()

                query = "select horarios_asignatura.codigo, horarios_asignatura.id, horarios_asignatura.nombre, horarios_asignatura.bloques, count(horarios_horario.asignatura_id) as cantidad, horarios_horario.curso_id  from horarios_asignatura, horarios_horario where horarios_asignatura.curso_id='" + str(idc) + "' and horarios_asignatura.id=horarios_horario.asignatura_id group by horarios_asignatura.id"
                with connection.cursor() as cursor:
                        cursor.execute(query)
                        results2 = cursor.fetchall()



                datos={"nomUsuario":nomUsuario,"asg":asg,"hor":hor,"pro2":pro2,"results": results, "results2": results2, "r2":'Debe Presionar el Boton para Continuar!!',"idc":idc, "hor2":hor2}
                return render(request,'modificar_horario.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#---------------------------------------------------------------------------------
def mostrarVisualizarHorario(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        cur=Curso.objects.all().order_by("id")
        datos={"nomUsuario":nomUsuario,"cur":cur}
        return render(request,'visualizar_horarios.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#--------------------------------------------------------------------------------
def buscarCurso(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if request.method=="POST":
            id=request.POST["opcur"]
            c=Curso.objects.filter(id=id)
            if c:
                comprobarHor=Horario.objects.filter(curso_id=id)
                if comprobarHor:
                    hor=Horario.objects.select_related("curso").filter(curso_id=id)
                    lun=Horario.objects.select_related("asignatura").filter(curso_id=id,dia="LUNES")
                    mar=Horario.objects.select_related("asignatura").filter(curso_id=id,dia="MARTES")
                    mie=Horario.objects.select_related("asignatura").filter(curso_id=id,dia="MIERCOLES")
                    jue=Horario.objects.select_related("asignatura").filter(curso_id=id,dia="JUEVES")
                    vie=Horario.objects.select_related("asignatura").filter(curso_id=id,dia="VIERNES")
                    cur=Curso.objects.all().order_by("id")
                    datos={"nomUsuario":nomUsuario,"cur":cur,"hor":hor,"r":'El Curso posee horario registrado!!'}
                    return render(request,'visualizar_horarios.html',datos)
                else:
                    cur=Curso.objects.all().order_by("id")
                    datos={"nomUsuario":nomUsuario,"cur":cur,"r3":'El Curso no posee Horario Registrado!!'}
                    return render(request,'visualizar_horarios.html',datos)
            else:
                cur=Curso.objects.all().order_by("id")
                datos={"nomUsuario":nomUsuario,"cur":cur,"r2":'Curso no Registrado!!'}
                return render(request,'visualizar_horarios.html',datos)
        else:
            cur=Curso.objects.all().order_by("id")
            datos={"nomUsuario":nomUsuario,"cur":cur,"r2":'Debe Presionar el Boton de Busqueda!!'}
            return render(request,'visualizar_horarios.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#----------------------------------------------------------------------------------------------
#----------------Disponibilidad-----------------------------------------------------------------
def mostrarVisualizarDisp(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        pro=Profesor.objects.all().order_by("rut")
        datos={"nomUsuario":nomUsuario,"pro":pro}
        return render(request,'visualizar_disponibilidad.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#---------------------------------------------------------------------------------
def mostrarRegistrarDis(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            rs=Profesor.objects.filter(id=id)
            if rs:
                dis=DisponibilidadProfesor.objects.filter(profesor_id=id)
                datos={"nomUsuario":nomUsuario,"rs":rs,"dis":dis}
                return render(request,'registrar_disponibilidad.html',datos)
            else:
                pro=Profesor.objects.all().values().order_by("rut")
                datos={"r2":'Profesor no registrado!!',"pro":pro,"nomUsuario":nomUsuario}
                return render(request,'registrar_profesor.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#----------------------------------------------------------------------------------
def buscarProfesorDis(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        p=Profesor.objects.filter(id=id)
        if p:
            comprobarDis=DisponibilidadProfesor.objects.filter(profesor_id=id)
            if comprobarDis:
                comprobarHor=Horario.objects.filter(profesor_id=id)
                if comprobarHor:
                    hor=Horario.objects.select_related("profesor").filter(profesor_id=id).order_by("curso_id")
                    lun1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=1).order_by("curso_id")
                    lun2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=2).order_by("curso_id")
                    lun3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=3).order_by("curso_id")
                    lun4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=4).order_by("curso_id")
                    lun5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=5).order_by("curso_id")
                    lun6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=6).order_by("curso_id")
                    lun7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=7).order_by("curso_id")
                    lun8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=8).order_by("curso_id")
                    lun9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=9).order_by("curso_id")
                    mar1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=1).order_by("curso_id")
                    mar2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=2).order_by("curso_id")
                    mar3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=3).order_by("curso_id")
                    mar4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=4).order_by("curso_id")
                    mar5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=5).order_by("curso_id")
                    mar6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=6).order_by("curso_id")
                    mar7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=7).order_by("curso_id")
                    mar8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=8).order_by("curso_id")
                    mar9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=9).order_by("curso_id")
                    mie1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=1).order_by("curso_id")
                    mie2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=2).order_by("curso_id")
                    mie3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=3).order_by("curso_id")
                    mie4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=4).order_by("curso_id")
                    mie5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=5).order_by("curso_id")
                    mie6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=6).order_by("curso_id")
                    mie7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=7).order_by("curso_id")
                    mie8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=8).order_by("curso_id")
                    mie9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=9).order_by("curso_id")
                    jue1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=1).order_by("curso_id")
                    jue2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=2).order_by("curso_id")
                    jue3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=3).order_by("curso_id")
                    jue4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=4).order_by("curso_id")
                    jue5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=5).order_by("curso_id")
                    jue6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=6).order_by("curso_id")
                    jue7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=7).order_by("curso_id")
                    jue8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=8).order_by("curso_id")
                    jue9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=9).order_by("curso_id")
                    vie1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=1).order_by("curso_id")
                    vie2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=2).order_by("curso_id")
                    vie3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=3).order_by("curso_id")
                    vie4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=4).order_by("curso_id")
                    vie5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=5).order_by("curso_id")
                    vie6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=6).order_by("curso_id")
                    vie7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=7).order_by("curso_id")
                    vie8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=8).order_by("curso_id")
                    vie9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=9).order_by("curso_id")
                    dis=DisponibilidadProfesor.objects.select_related("profesor").filter(profesor_id=id)
                    rs=Profesor.objects.filter(id=id)
                    pro=Profesor.objects.all().order_by("rut")
                    datos={"nomUsuario":nomUsuario,"pro":pro,"dis":dis,"rs":rs,"r":'El Profesor Posee Disponibilidad Registrada!!',"lun1":lun1,"lun2":lun2,"lun3":lun3,"lun4":lun4,"lun5":lun5,"lun6":lun6,"lun7":lun7,"lun8":lun8,"lun9":lun9,"mar1":mar1,"mar2":mar2,"mar3":mar3,"mar4":mar4,"mar5":mar5,"mar6":mar6,"mar7":mar7,"mar8":mar8,"mar9":mar9,"mar1":mie1,"mie2":mie2,"mie3":mie3,"mie4":mie4,"mie5":mie5,"mie6":mie6,"mie7":mie7,"mie8":mie8,"mie9":mie9,"jue1":jue1,"jue2":jue2,"jue3":jue3,"jue4":jue4,"jue5":jue5,"jue6":jue6,"jue7":jue7,"jue8":jue8,"jue9":jue9,"vie1":vie1,"vie2":vie2,"vie3":vie3,"vie4":vie4,"vie5":vie5,"vie6":vie6,"vie7":vie7,"vie8":vie8,"vie9":vie9,"hor":hor}
                    return render(request,'visualizar_disponibilidad.html',datos)
                else:
                    dis=DisponibilidadProfesor.objects.select_related("profesor").filter(profesor_id=id)
                    rs=Profesor.objects.filter(id=id)
                    pro=Profesor.objects.all().order_by("rut")
                    datos={"nomUsuario":nomUsuario,"pro":pro,"dis":dis,"rs":rs,"r":'El Profesor Posee Disponibilidad Registrada!!'}
                    return render(request,'visualizar_disponibilidad.html',datos)
            else:
                pro=Profesor.objects.all().order_by("rut")
                datos={"nomUsuario":nomUsuario,"pro":pro,"r3":'El Profesor no Posee Disponibilidad Registrada!!'}
                return render(request,'visualizar_disponibilidad.html',datos)
        else:
            pro=Profesor.objects.all().order_by("rut")
            datos={"nomUsuario":nomUsuario,"pro":pro,"r2":'Profesor no Registrado!!'}
            return render(request,'visualizar_disponibilidad.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-------------------------------------------------------------------------------------------
def cambiarDisponibilidad(request,id,id2):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            dis=DisponibilidadProfesor.objects.filter(id=id)
            if dis:
                d=DisponibilidadProfesor.objects.get(id=id)
                dia=d.dia
                es=d.estado
                bl=d.bloque
                if es == "NO DISPONIBLE":
                    d.estado="DISPONIBLE"
                    est="DISPONIBLE"
                else:
                    d.estado="NO DISPONIBLE"
                    est="NO DISPONIBLE"
                    h=Horario.objects.filter(profesor_id=id2,bloque=bl)                          #Registro de Disponibilidad
                    if h:                                                                                #Metodo para alterar los Horarios sin eliminar datos que se desean conservar
                        j=0
                        for x in h:
                            if x == h[j]:
                                y=Horario.objects.get(id=h[j].id)
                                y.profesor_id=""
                                y.asignatura_id=""
                                y.save()

                            j=j+1
                d.save()
                p=Profesor.objects.get(id=id2)
                pr=p.rut
                des="Cambio de Disponibilidad ("+str(dia)+") estado ("+str(est)+") de Profesor "+str(pr)+""
                tabla="DisponibilidadProfesor"
                fyh=datetime.now()
                usuario=request.session.get("idUsuario")
                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                his.save()
                rs=Profesor.objects.filter(id=id2)
                dis=DisponibilidadProfesor.objects.filter(profesor_id=id2)
                datos={"nomUsuario":nomUsuario,"rs":rs,"dis":dis,"r":'Disponibilidad Modificada Correctamente!!'}
                return render(request, 'registrar_disponibilidad.html',datos)
            else:
                rs=Profesor.objects.filter(id=id2)
                dis=DisponibilidadProfesor.objects.filter(profesor_id=id2)
                datos={"nomUsuario":nomUsuario,"rs":rs,"dis":dis,"r2":'Debe Seleccionar un Bloque para Modifiacar!!'}
                return render(request, 'registrar_especialidad.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-----------------------Especialidades del Profesor-------------------------
def mostrarRegistrarEsp(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            rs=Profesor.objects.filter(id=id)
            esp=AsignaturasProfesor.objects.filter(profesor_id=id)
            asi=Asignatura.objects.all().values()
            datos={"nomUsuario":nomUsuario,"rs":rs,"esp":esp,"asi":asi}
            return render(request, 'registrar_especialidad.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-------------------------------------------------------------------------------------------
def registrarEspecialidad(request,id):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            if request.method=="POST":
                    asg=request.POST["opasg"]
                    #niv=request.POST["opniv"]
                    niv='BASICA y MEDIA'
                    #if (asg=="Biología" or asg=="Química" or asg=="Física" or asg=="Filosofía y Psicología") and niv=="BASICA":
                    #    rs=Profesor.objects.filter(id=id)
                    #    esp=AsignaturasProfesor.objects.filter(profesor_id=id)
                    #    datos={"nomUsuario":nomUsuario,"rs":rs,"esp":esp,"r2":'La Asignatura no corresponde al nivel seleccionado!!'}
                    #    return render(request, 'registrar_especialidad.html',datos)
                    #else:
                    es=AsignaturasProfesor.objects.filter(nombre_especialidad=asg,profesor_id=id,nivel_especialidad=niv)
                    if es:
                        rs=Profesor.objects.filter(id=id)
                        esp=AsignaturasProfesor.objects.filter(profesor_id=id)
                        asi=Asignatura.objects.all().values()
                        datos={"nomUsuario":nomUsuario,"rs":rs,"asi":asi,"esp":esp,"r2":'La Especialidad "'+str(asg)+' ('+str(niv)+')" ya esta Registrada!!'}
                        return render(request, 'registrar_especialidad.html',datos)
                    else:
                        e=AsignaturasProfesor(nombre_especialidad=asg,nivel_especialidad=niv,profesor_id=id)
                        e.save()
                        p=Profesor.objects.get(id=id)
                        pr=p.rut
                        des="Registro de Especialidad "+str(pr)+""
                        tabla="AsignaturasProfesor"
                        fyh=datetime.now()
                        usuario=request.session.get("idUsuario")
                        his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                        his.save()
                        rs=Profesor.objects.filter(id=id)
                        esp=AsignaturasProfesor.objects.filter(profesor_id=id)
                        asi=Asignatura.objects.all().values()
                        datos={"nomUsuario":nomUsuario,"rs":rs,"asi":asi,"esp":esp,"r":'Especialidades Registradas Correctamente!!'}
                        return render(request, 'registrar_especialidad.html',datos)
            else:
                rs=Profesor.objects.filter(id=id)
                esp=AsignaturasProfesor.objects.filter(profesor_id=id)
                datos={"nomUsuario":nomUsuario,"rs":rs,"esp":esp,"r2":'Debe Presionar El Boton de Registro!!'}
                return render(request, 'registrar_especialidad.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-----------------------------------------------------------------------------
def eliminarEspecialidad(request,id,id2):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="SECRETARIA":
            esp=AsignaturasProfesor.objects.filter(id=id)
            if esp:
                e=AsignaturasProfesor.objects.get(id=id)
                nom=e.nombre_especialidad
                niv=e.nivel_especialidad
                a=Asignatura.objects.filter(nombre=nom,nivel=niv)
                h=Horario.objects.filter(profesor_id=id2)
                if h and a:
                    j=0
                    for x in h:
                        if x == h[j] and h[j].asignatura_id == a[0].id:
                            y=Horario.objects.get(id=h[j].id)
                            y.profesor_id=""
                            y.asignatura_id=""
                            y.save()
                        j=j+1
                esp.delete()
                p=Profesor.objects.get(id=id2)
                pr=p.rut
                des="Eliminacion de Registro ("+str(nom)+") nivel ("+str(niv)+") de Profesor "+str(pr)+""
                tabla="AsignaturasProfesor"
                fyh=datetime.now()
                usuario=request.session.get("idUsuario")
                his=Historial(accion=des,tabla=tabla,fecha=fyh,usuario_id=usuario)
                his.save()
                rs=Profesor.objects.filter(id=id2)
                esp=AsignaturasProfesor.objects.filter(profesor_id=id2)
                datos={"nomUsuario":nomUsuario,"rs":rs,"esp":esp,"r":'Especialidad Eliminada Correctamente!!'}
                return render(request, 'registrar_especialidad.html',datos)
            else:
                rs=Profesor.objects.filter(id=id2)
                esp=AsignaturasProfesor.objects.filter(profesor_id=id2)
                datos={"nomUsuario":nomUsuario,"rs":rs,"esp":esp,"r2":'Debe Seleccionar una Especialidad para Eliminar!!'}
                return render(request, 'registrar_especialidad.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#----------------------------Historial----------------------------------------------
def mostrarHistorial(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if nomUsuario=="DIRECTORA":
            his=Historial.objects.all().order_by("-fecha")
            datos={"his":his,"nomUsuario":nomUsuario}
            return render(request,'listar_historial.html',datos)
        else:
            datos={"r2":'No tiene permisos para acceder a esta Pagina!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
            return render(request,'index.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#--------------------------------------------------------------------------------------------------
def buscarProfesor(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        if request.method=="POST":
            id=request.POST["oppro"]
            p=Profesor.objects.filter(id=id)
            if p:
                comprobarHor=Horario.objects.filter(profesor_id=id)
                if comprobarHor:
                    hor=Horario.objects.select_related("profesor").filter(profesor_id=id).order_by("curso_id")
                    lun1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=1).order_by("curso_id")
                    lun2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=2).order_by("curso_id")
                    lun3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=3).order_by("curso_id")
                    lun4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=4).order_by("curso_id")
                    lun5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=5).order_by("curso_id")
                    lun6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=6).order_by("curso_id")
                    lun7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=7).order_by("curso_id")
                    lun8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=8).order_by("curso_id")
                    lun9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="LUNES",bloque=9).order_by("curso_id")
                    mar1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=1).order_by("curso_id")
                    mar2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=2).order_by("curso_id")
                    mar3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=3).order_by("curso_id")
                    mar4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=4).order_by("curso_id")
                    mar5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=5).order_by("curso_id")
                    mar6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=6).order_by("curso_id")
                    mar7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=7).order_by("curso_id")
                    mar8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=8).order_by("curso_id")
                    mar9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MARTES",bloque=9).order_by("curso_id")
                    mie1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=1).order_by("curso_id")
                    mie2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=2).order_by("curso_id")
                    mie3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=3).order_by("curso_id")
                    mie4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=4).order_by("curso_id")
                    mie5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=5).order_by("curso_id")
                    mie6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=6).order_by("curso_id")
                    mie7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=7).order_by("curso_id")
                    mie8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=8).order_by("curso_id")
                    mie9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="MIERCOLES",bloque=9).order_by("curso_id")
                    jue1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=1).order_by("curso_id")
                    jue2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=2).order_by("curso_id")
                    jue3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=3).order_by("curso_id")
                    jue4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=4).order_by("curso_id")
                    jue5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=5).order_by("curso_id")
                    jue6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=6).order_by("curso_id")
                    jue7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=7).order_by("curso_id")
                    jue8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=8).order_by("curso_id")
                    jue9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="JUEVES",bloque=9).order_by("curso_id")
                    vie1=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=1).order_by("curso_id")
                    vie2=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=2).order_by("curso_id")
                    vie3=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=3).order_by("curso_id")
                    vie4=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=4).order_by("curso_id")
                    vie5=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=5).order_by("curso_id")
                    vie6=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=6).order_by("curso_id")
                    vie7=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=7).order_by("curso_id")
                    vie8=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=8).order_by("curso_id")
                    vie9=Horario.objects.select_related("asignatura","curso").filter(profesor_id=id,dia="VIERNES",bloque=9).order_by("curso_id")
                    pro=Profesor.objects.all().order_by("id")
                    rs=Profesor.objects.filter(id=id)
                    datos={"nomUsuario":nomUsuario,"pro":pro,"hor":hor,"r":'El Profesor posee horario registrado!!',"rs":rs,"lun1":lun1,"lun2":lun2,"lun3":lun3,"lun4":lun4,"lun5":lun5,"lun6":lun6,"lun7":lun7,"lun8":lun8,"lun9":lun9,"mar1":mar1,"mar2":mar2,"mar3":mar3,"mar4":mar4,"mar5":mar5,"mar6":mar6,"mar7":mar7,"mar8":mar8,"mar9":mar9,"mar1":mie1,"mie2":mie2,"mie3":mie3,"mie4":mie4,"mie5":mie5,"mie6":mie6,"mie7":mie7,"mie8":mie8,"mie9":mie9,"jue1":jue1,"jue2":jue2,"jue3":jue3,"jue4":jue4,"jue5":jue5,"jue6":jue6,"jue7":jue7,"jue8":jue8,"jue9":jue9,"vie1":vie1,"vie2":vie2,"vie3":vie3,"vie4":vie4,"vie5":vie5,"vie6":vie6,"vie7":vie7,"vie8":vie8,"vie9":vie9}
                    return render(request,'visualizar_horarios_profesor.html',datos)
                else:
                    pro=Profesor.objects.all().order_by("id")
                    datos={"nomUsuario":nomUsuario,"pro":pro,"r3":'El Profesor no posee Horario Registrado!!'}
                    return render(request,'visualizar_horarios_profesor.html',datos)
            else:
                pro=Profesor.objects.all().order_by("id")
                datos={"nomUsuario":nomUsuario,"pro":pro,"r2":'Profesor no Registrado!!'}
                return render(request,'visualizar_horarios_profesor.html',datos)
        else:
            pro=Profesor.objects.all().order_by("id")
            datos={"nomUsuario":nomUsuario,"pro":pro,"r2":'Debe Presionar el Boton de Busqueda!!'}
            return render(request,'visualizar_horarios_profesor.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)
#-------------------------------------------------------------------------
def mostrarHorarioProfesor(request):
    nomUsuario=request.session.get("nomUsuario")
    if nomUsuario:
        pro=Profesor.objects.all().order_by("id")
        datos={"nomUsuario":nomUsuario,"pro":pro}
        return render(request,'visualizar_horarios_profesor.html',datos)
    else:
        datos={"r2":'Debe Iniciar Sesion!!',"uc":'Cursos y Usuarios cargados correctamente!!'}
        return render(request,'index.html',datos)