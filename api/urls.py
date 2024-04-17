from django.urls import path
from . import views

urlpatterns=[
    path('all_users/',views.getusers),
    path('add_user/',views.adduser),
    path('verify_user/',views.verifyuser)


    ]