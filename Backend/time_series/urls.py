from django.urls import path
from . import views

app_name = 'time_series' # Allows for redirect from roles app 

urlpatterns = [
  ### GET urls (public) - render pages ###
  path('', views.redirect_home),
  path('home/', views.home_page, name='index_html'),
  path('contributor/', views.contributor, name='contributor_html'),
  path('mle/', views.mle, name='mle_html'),
  path('mle/solution/', views.solution, name='solution_html'),
  path('admin/', views.admin, name='admin_html'),
  
  ### POST urls (private) ###
  path('_upload-data/', views.upload_data), 
  path('_solution/', views.upload_solution),
  
  ### GET urls (private) ###
  path('_get-solution/', views.get_solutions_request),
  path('_get-train-data/', views.train_data_pull_request),
  path('_download-train-data/', views.download_train_data),
  
  path('home/login/', views.login),
]