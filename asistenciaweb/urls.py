from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asistenciaweb.views.home', name='home'),
    # url(r'^asistenciaweb/', include('asistenciaweb.foo.urls')),
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
