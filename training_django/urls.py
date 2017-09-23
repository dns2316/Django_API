from django.conf.urls import url, include
from django.contrib import admin
from movie_app import views

urlpatterns = [
    url(r'^movie/', include('movie_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', views.error, name='error'),
]
