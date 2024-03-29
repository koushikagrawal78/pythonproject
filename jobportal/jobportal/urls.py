"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from testapp import views
from django.contrib.auth import views as auth_views
#Add Django site authentication urls (for login, logout, password management)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index', views.index),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^hydjobs/', views.hydjobs1),
    url(r'^bengjobs/', views.bengjobs1),
    url(r'^chenjobs/', views.chenjobs1),
    url(r'^punejobs/', views.punejobs1),
    url(r'^mumjobs/', views.mumjobs1),
    url(r'^logout123/', views.logout_view),
    url(r'^signup/',views.signup_view1 ),
    url(r'^account/',include('django.contrib.auth.urls')),
]
