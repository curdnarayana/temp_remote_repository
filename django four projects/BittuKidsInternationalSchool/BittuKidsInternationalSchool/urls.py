from django.conf.urls import url
from django.contrib import admin
from django.http.response import HttpResponse
from BittuApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home),
    url(r'^$',views.home),
    # url(r'^history/',views.history),
    url(r'^history/',views.history),
    url(r'^management/',views.management),
    url(r'^ourmission/',views.our_mission),
    url(r'^rules/',views.rules),
    url(r'^sportiva/',views.sportiva),
    url(r'^exubarence/',views.exubarence),
    url(r'^about/',views.about),
    url(r'^events/',views.events),
]
