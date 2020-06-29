from django.conf.urls import url
from django.urls import path,include
from basic_apps import views


app_name = 'basic_apps'


urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
