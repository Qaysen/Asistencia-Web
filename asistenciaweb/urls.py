from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),   
    url(r'^admin/', include(admin.site.urls)),
    #orlando
    url(r'^turno/$', 'principal.views.turno'),
    url(r'^ajax/agregar-turno/$', 'principal.views.agregar_turno'),
    url(r'^ajax/eliminar-turno/$', 'principal.views.eliminar_turno'),     
    url(r'^edit_nombre/$', 'principal.views.edit_nombre'),    
   
)
 