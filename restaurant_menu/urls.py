from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from menu.views import menu

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurant_menu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',menu),
)
