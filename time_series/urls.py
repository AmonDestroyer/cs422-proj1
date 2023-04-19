from django.urls import path
from . import views

app_name = 'time_series'

urlpatterns = [
  path('', views.redirect_home),
  path('home/', views.home_page),
  path('contributor/', views.contributor, name='contributor_html'),
  path('mle/', views.mle, name='mle_html'),
  path('admin/', views.admin, name='admin_html'),
  
  path('home/login/', views.login),
]