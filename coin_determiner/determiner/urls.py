from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'coin_determiner.determiner.views.index', name='index'),
]
