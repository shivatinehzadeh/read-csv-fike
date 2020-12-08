from django.urls import path
from . import views

app_name='CSV'

urlpatterns=[
path('',views.read_csv,name='readFile'),
path('email/',views.Send_mail.as_view(),name='email'),
]