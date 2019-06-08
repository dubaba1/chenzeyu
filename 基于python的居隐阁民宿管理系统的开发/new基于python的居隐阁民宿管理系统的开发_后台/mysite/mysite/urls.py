"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from cmdb import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'add_user/', views.add_user),
    path(r'login_user/', views.login_user),
    path(r'select/one/login_user/', views.login_user),
    path(r'select_all_user/', views.select_all_user),
    path(r'del_user/', views.del_user),
    path(r'add_home/', views.add_home),
    path(r'del_home/', views.del_home),
    path(r'select_all_home/', views.select_all_home),
    path(r'xiandan/', views.xiandan),
    path(r'check_in_data/',views.check_in_data),
    path(r'check_in_data/',views.check_in_data),
    path(r'check_in/',views.check_in),
    path(r'select_in_dianpu/',views.select_in_dianpu),
    path(r'check_out/',views.check_out),
    path(r'select_all_user_order/',views.select_all_user_order),
    path(r'insert_gonggao/',views.insert_gonggao),
    path(r'select_gonggao/',views.select_gonggao),
    path(r'select_out_dianpu/',views.select_out_dianpu),
    path(r'into_plun/',views.into_plun),
]
