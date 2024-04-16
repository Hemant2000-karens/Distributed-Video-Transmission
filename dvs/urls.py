"""
URL configuration for dvs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from dvs_app import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view,name='login'),
    path('homepage/', views.home_view, name='homepage'),
    path('logout/',views.logout_view, name='logout'),
    #path('show_broadcast/', views.show_broadcast, name='show_broadcast'),
    path('update_watch_count/', views.update_watch_count, name='update_watch_count'),
    path('some-action/<str:codec>/', views.my_view, name='my-view'),
]

# print("BASE_DIR:", path('show_broadcast/'))