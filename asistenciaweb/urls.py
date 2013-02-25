from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',   
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^usuarios/registrar/$','principal.views.registrar_usuario'),
    url(r'^usuarios/editar/(?P<id_usuario>\d+)$', 'principal.views.editar_usuario'),
    url(r'^resetear_clave/$', 'principal.views.resetear_clave'),
    url(r'^edit_nombre/$', 'principal.views.edit_nombre'), 
    #url(r'^usuarioTurno/$', 'principal.views.usuarioTurno'),
    #url(r'^ver_usuarios/$', 'principal.views.ver_usuarios'),
    #url(r'^edit_fechas/$', 'principal.views.edit_fechas'),    
    #url(r'^edit_usuario/$', 'principal.views.edit_usuario'), 
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^descuentos/', 'principal.views.descuentos'),
    url(r'^grafico-descuentos/', 'principal.views.graficos_descuentos'),
    url(r'^controles/', 'principal.views.controles'),
    url(r'^registrar-controles/', 'principal.views.registrar_controles'),
    url(r'^turno/$', 'principal.views.turno'),
    
    url(r'^ajax/agregar-turno/$', 'principal.views.agregar_turno'),
    url(r'^ajax/eliminar-turno/$', 'principal.views.eliminar_turno'), 
    url(r'^ajax/registrar-descuento/', 'principal.views.agregar_descuento'),
    url(r'^ajax/registrar-control/', 'principal.views.agregar_control'),
    url(r'^ajax/eliminar-descuento/', 'principal.views.eliminar_descuento'),
    url(r'^ajax/usuarios/', 'principal.views.ajax_usuarios'),
    url(r'^ajax/editar-descuento/', 'principal.views.editar_descuento'),
    url(r'^ajax_ver_usuario/$','principal.views.ajax_ver_usuario'),    
    url(r'^ajax-username/$', 'principal.views.ajax_username'),
    #url(r'^ajax/agregarUT/$', 'principal.views.agregarUT'),
    #url(r'^ajax/eliminarUT/$', 'principal.views.eliminarUT'),  
)
 
