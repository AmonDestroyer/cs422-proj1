from django.urls import path
from . import views

urlpatterns = [
  path('', views.login_page),
  path('<str:role>.html/', views.redirect_to_time_series),
  path('<str:role>.css/', views.redirect_to_time_series),
  path('<str:role>.js/', views.redirect_to_time_series),
]