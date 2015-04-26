from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'coin_determiner.views.home', name='home'),
    url(r'^$', include('coin_determiner.determiner.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
