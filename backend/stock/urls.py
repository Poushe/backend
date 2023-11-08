from django.urls import path
from . import views

urlpatterns=[
    path('',views.stock),
    path('restricted', views.loginrestricted, name='restricted'),
    path('income', views.incomeform, name='incomeform'),
    path('expense', views.expenseform, name='expenseform'),
    path('allincome', views.allincome, name='allincome'),
    path('allexpense', views.allexpense, name='allexpense'),
]