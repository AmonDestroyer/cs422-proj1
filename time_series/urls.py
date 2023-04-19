from django.urls import path
from . import views

app_name = 'time_series'

urlpatterns = [
  path('', views.home_page),
  path('contributor', views.contributor, name='contributor_html'),
  path('mle', views.mle, name='mle_html'),
  path('admin', views.admin, name='admin_html'),
]