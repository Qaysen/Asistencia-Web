from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asistenciaweb.views.home', name='home'),
    # url(r'^asistenciaweb/', include('asistenciaweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^descuentos/', 'principal.views.descuentos'),
    url(r'^grafico-descuentos/', 'principal.views.graficos_descuentos'),
    url(r'^controles/', 'principal.views.controles'),
    url(r'^registrar-controles/', 'principal.views.registrar_controles'),
    url(r'^ajax/registrar-descuento/', 'principal.views.agregar_descuento'),
    url(r'^ajax/registrar-control/', 'principal.views.agregar_control'),
    url(r'^ajax/eliminar-descuento/', 'principal.views.eliminar_descuento'),
    url(r'^ajax/usuarios/', 'principal.views.ajax_usuarios'),

    url(r'^ajax/editar-descuento/', 'principal.views.editar_descuento'),
)
