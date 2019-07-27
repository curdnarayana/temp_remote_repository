from django.conf.urls import url
from django.contrib import admin
from matrimonyapp import views

urlpatterns = {
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.loginview),
    url(r'^registration/', views.registrationview),
    url(r'^home/', views.home),
    url(r'^services/', views.services),
    url(r'clients', views.clients),
    url(r'^boys', views.boys),
    url(r'^girls', views.girls),
    url(r'gallery', views.gallery),
    url(r'feedback', views.feedback),
    url(r'^login/', views.loginview),
    url(r'^password/', views.password),
    url(r'^team',views.team)
}
