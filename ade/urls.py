from django.conf.urls import patterns, include, url
from addr_book.views import *
from django.contrib import admin
admin.autodiscover()
# aa
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ade.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/', add),
    url(r'^look/', look),
    url(r'^delete/$', delete),
    url(r'^search_author/', search_author),
    url(r'^information/$', information),
)
