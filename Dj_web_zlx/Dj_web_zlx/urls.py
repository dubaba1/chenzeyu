from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from . import view,testdb,search
from  TestModel import views

urlpatterns = [

    path('testdb', testdb.testdb),
    path('shop1/', views.sp1),
    path('shop2/', views.sp2),
    path('shop3/', views.sp3),
    path('shop4/', views.sp4),
    path('shop5/', views.sp5),
    path('shop6/', views.sp6),
    path('shop7/', views.sp7),
    path('shop8/', views.sp8),
    path('shop9/', views.sp9),
    path('index/', views.index),


]
urlpatterns += staticfiles_urlpatterns()