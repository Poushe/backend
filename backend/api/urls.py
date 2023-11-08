from django.urls import path
from . import views
urlpatterns=[
    path('',views.getUrl,name='geturl'),
]