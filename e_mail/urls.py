from django.urls import path
from e_mail import views


urlpatterns=[
    path('login',views.login),
    path('register',views.register),
    path('bind',views.bind_email_login)
]