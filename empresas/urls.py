from django.urls import path
from . import views


urlpatterns = [
    # The home page
    path(r'', views.administracion, name='administracion'),

    #URL HISTORIA
    path(r'historia', views.historia, name='historia'),
    path(r'historia_list', views.historia_list, name='historia_list'),
    path(r'historia_edit/<int:pk>/', views.historia_edit, name='historia_edit'),
    path(r'historia_detail/<int:pk>/', views.HistoriaDetail.as_view(), name='historia_detail'),
    path(r'historia_delete/<int:pk>/', views.HistoriaDelete.as_view(), name='historia_delete'),


    #URL TEAM
    path(r'team', views.team, name='team'),
    path(r'team_list', views.team_list, name='team_list'),
    path(r'team_edit/<int:pk>/', views.team_edit, name='team_edit'),
    path(r'team_detail/<int:pk>/', views.TeamDetail.as_view(), name='team_detail'),
    path(r'team_delete/<int:pk>/', views.TeamDelete.as_view(), name='team_delete'),

    #URL PLAN corporativo
    path(r'plan', views.plan, name='plan'),
    path(r'plan_list', views.plan_list, name='plan_list'),
    path(r'plan_edit/<int:pk>/', views.plan_edit, name='plan_edit'),
    path(r'plan_detail/<int:pk>/', views.PlanDetail.as_view(), name='plan_detail'),
    path(r'plan_delete/<int:pk>/', views.PlanDelete.as_view(), name='plan_delete'),

]
