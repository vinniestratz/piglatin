from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^translate/', views.translate, name='translate'),
    url(r'^admin/', admin.site.urls),
]
