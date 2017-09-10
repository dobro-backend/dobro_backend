from django.conf.urls import url, include
from dobro import views

urlpatterns = [
    url(r'^signup', views.signup),
]