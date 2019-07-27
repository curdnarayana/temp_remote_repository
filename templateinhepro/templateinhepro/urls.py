from django.conf.urls import url
from django.contrib import admin
from templateinheapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_page_view),
    url(r'^home/',views.home_page_view),
    url(r'^contact/',views.contact_page_view),
    url(r'^feedback/',views.feedback_page_view),
    url(r'^services/',views.services_page_view)
]





