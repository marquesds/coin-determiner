from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('coin_determiner.determiner.urls', namespace='determiner')),

    url(r'^admin/', include(admin.site.urls)),
]
