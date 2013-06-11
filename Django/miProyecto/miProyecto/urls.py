from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miProyecto.views.home', name='home'),
    url(r'^demo/', 'demo.views.home'),
    url(r'^post/(\d{1,2})/$', 'demo.views.post'),
    url(r'^hora/$', 'demo.views.hora'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
