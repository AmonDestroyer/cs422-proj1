from django.urls import path
from . import views

app_name = 'roles'

urlpatterns = [
  path('', views.login_page, name='login'),
  path('<str:role>.html/', views.redirect_to_time_series),
  path('<str:role>.css/', views.redirect_to_time_series),
  path('<str:role>.js/', views.redirect_to_time_series),
]