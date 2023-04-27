from django.urls import path
from . import views

app_name = 'time_series'

urlpatterns = [
  path('', views.redirect_home),
  path('home/', views.home_page, name='index_html'),
  path('contributor/', views.contributor, name='contributor_html'),
  path('mle/', views.mle, name='mle_html'),
  path('admin/', views.admin, name='admin_html'),
  
  # POST urls
  path('_upload-data/', views.upload_data), # name subject to change
  
  
  path('home/login/', views.login),
]