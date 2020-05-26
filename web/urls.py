from django.urls import path,re_path
from django.contrib import admin

from . import views

urlpatterns = [
    #path('index/', views.index, name='main-view'),
    #path('', views.submit_expense,name='submit_expense'),
    #path("", views.index, name="index"),
    re_path(r'^submit/expense/$', views.submit_expense,name='submit_expense'),
    re_path(r'^submit/income/$', views.submit_income,name='submit_income'),
    ]
