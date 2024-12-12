"""
URL configuration for Ins_Lautaro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from horarios import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
#-----------------General----------------------------------------------------------------------------
    path('admin/', admin.site.urls),
    path('',views.mostrarIndex),
    path('login',views.iniciarSesion),
    path('logout',views.cerrarSesion),
    path('registrar_usu',views.registrarUsuarios),
    path('registrar_cur',views.registrarCursos),
    path('visualizar_horarios',views.mostrarVisualizarHorario),
    path('visuzalizar_disponibilidad',views.mostrarVisualizarDisp),
    path('buscar_dis/<int:id>',views.buscarProfesorDis),
    path('buscar_cur',views.buscarCurso),
    path('visualizar_horarios_profesores',views.mostrarHorarioProfesor),
    path('buscar_pro',views.buscarProfesor),
#---------------------------Directora---------------------------------------------------------------
    path('menu_directora',views.mostrarMenuDirectora),
    path('visualizar_historial',views.mostrarHistorial),
#---------------------------Secretaria---------------------------------------------------------------
    path('menu_secretaria',views.mostrarMenuSecretaria),
    #-----------------------Asignaturas-----------------------------------------
    path('registrar_asignaturas',views.mostrarRegistrarAsig),
    path('modificar_asignatura/<int:id>',views.mostrarModificarAsig),
    path('registrar_asg',views.registrarAsignatura),
    path('modificar_asg/<int:id>',views.modificarAsignatura),
    path('eliminar_asg/<int:id>',views.eliminarAsignatura),
    #---------------------Profesores---------------------------------------------
    path('registrar_profesor',views.mostrarRegistrarPro),
    path('modificar_profesor/<int:id>',views.mostrarModificarPro),
    path('registrar_pro',views.registrarProfesor),
    path('modificar_pro/<int:id>',views.modificarProfesor),
    path('eliminar_pro/<int:id>',views.eliminarProfesor),
    #--------------------Horarios-------------------------------------------------
    path('registrar_horarios',views.mostrarRegistrarHor),
    path('mostrar_horario/<int:id>/<int:idc>',views.mostrarHorario),
    path('cambiar_hor/<int:id>/<int:idc>',views.cambiarHorario),
    #--------------------Disponibilidad------------------------------------------
    path('registrar_disponibilidad/<int:id>',views.mostrarRegistrarDis),
    path('cambiar_disponibilidad/<int:id>/<int:id2>',views.cambiarDisponibilidad),
    #------------------Especialidades (Asignaturas) Porfesor-----------------------------------------------
    path('registrar_especialidad/<int:id>',views.mostrarRegistrarEsp),
    path('registrar_esp/<int:id>',views.registrarEspecialidad),
    path('eliminar_esp/<int:id>/<int:id2>',views.eliminarEspecialidad),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)