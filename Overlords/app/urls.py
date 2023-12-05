from django.urls import path
from . import views
from .views import usuario

urlpatterns = [
    path ('', views.home, name='home_app'),
    path ('get_data/', views.get_data, name='get_app'),
    path ('add_data/', views.add_data, name='add_app'),
    path ('del_data/<int:id>/', views.del_data, name='del_app'),
    path ('edit_data/', views.edit_data, name='edit_app'),
    path ('usuario', views.usuario, name='usuario')
]