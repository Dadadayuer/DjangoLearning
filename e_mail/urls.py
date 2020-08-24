from django.urls import path
from e_mail import views


urlpatterns=[
    path('login',views.login),
]