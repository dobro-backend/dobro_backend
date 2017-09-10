from django.conf.urls import include, url
from dobro import views


urlpatterns = [
    url(r'^api/signup', views.signup),
    url(r'^api/auth', views.auth),
]
