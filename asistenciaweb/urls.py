from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asistenciaweb.views.home', name='home'),
    # url(r'^asistenciaweb/', include('asistenciaweb.foo.urls')),

    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^usuarios/registrar/$','principal.views.registrar_usuario'),
    url(r'^usuarios/editar/(?P<id_usuario>\d+)$', 'principal.views.editar_usuario'),
    url(r'^ajax_ver_usuario/$','principal.views.ajax_ver_usuario'),    
    url(r'^ajax-username/$', 'principal.views.ajax_username'),
    url(r'^resetear_clave/$', 'principal.views.resetear_clave'),

    url(r'^usuarioTurno/$', 'principal.views.usuarioTurno'),
    url(r'^ver_usuarios/$', 'principal.views.ver_usuarios'),
    url(r'^edit_fechas/$', 'principal.views.edit_fechas'),    
    url(r'^edit_usuario/$', 'principal.views.edit_usuario'),
    url(r'^ajax/agregarUT/$', 'principal.views.agregarUT'),
    url(r'^ajax/eliminarUT/$', 'principal.views.eliminarUT'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
