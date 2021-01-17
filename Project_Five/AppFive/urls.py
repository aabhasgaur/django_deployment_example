from django.conf.urls import url
from AppFive import views

#TEMPLATE URLs
app_name = 'AppFive'

urlpatterns=[
    url('registeration/',views.register,name='registeration'),
    url('user_login/',views.user_login,name='user_login'),
]
