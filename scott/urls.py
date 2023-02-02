from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('trade_bot/', views.trade_bot, name= 'trade_bot'),
    path('bg_nav/', views.bg_nav, name= 'bg_nav'),
    path('certif/', views.certif, name= 'certif'),
    path('web_react/', views.web_react, name= 'web_react'),
    path('roster/', views.roster, name='roster'),
    path('team_creator/', views.team_creator, name='team_creator'),
    path('prof_exp/', views.prof_exp, name='prof_exp'),
    path('flask/', views.flask, name='flask_site'),
    path('fastapi/', views.fastapi, name='API_Endpoint'),
]