from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',   
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^usuarios/registrar/$','principal.views.registrar_usuario'),
    url(r'^usuarios/editar/(?P<id_usuario>\d+)$', 'principal.views.editar_usuario'),
    url(r'^ajax_ver_usuario/$','principal.views.ajax_ver_usuario'),    
    url(r'^ajax-username/$', 'principal.views.ajax_username'),
    url(r'^resetear_clave/$', 'principal.views.resetear_clave'),
    #elicia
    url(r'^usuarioTurno/$', 'principal.views.usuarioTurno'),
    url(r'^ver_usuarios/$', 'principal.views.ver_usuarios'),
    url(r'^edit_fechas/$', 'principal.views.edit_fechas'),    
    url(r'^edit_usuario/$', 'principal.views.edit_usuario'),
    url(r'^ajax/agregarUT/$', 'principal.views.agregarUT'),

    url(r'^ajax/eliminarUT/$', 'principal.views.eliminarUT'),   
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^ajax/eliminarUT/$', 'principal.views.eliminarUT'),      
    url(r'^admin/', include(admin.site.urls)),
    #orlando
    url(r'^turno/$', 'principal.views.turno'),
    url(r'^ajax/agregar-turno/$', 'principal.views.agregar_turno'),
    url(r'^ajax/eliminar-turno/$', 'principal.views.eliminar_turno'),     
    url(r'^edit_nombre/$', 'principal.views.edit_nombre'),    
   
)
 
