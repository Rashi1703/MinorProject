from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('register/', views.register, name='register'),
    path('signup/', views.signup, name='signup'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('send_password/', views.send_password, name='send_password')
]

