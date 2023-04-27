from django.urls import path
from . import views

app_name = 'roles'

urlpatterns = [
  path('', views.login_page, name='login'),
  path('<str:file>.html/', views.redirect_to_time_series),
]