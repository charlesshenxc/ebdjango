from django.urls import path

from . import views

urlpatterns = [
    # ex: /survey/
    path('', views.index, name='index'),
    path('create_survey', views.create_survey, name='create_survey'),
    path('create_question/<uuid:survey_id>/', views.create_question, name='create_question'),
    path('delete_survey/<uuid:survey_id>/', views.delete_survey, name='delete_survey'),
    path('result/<uuid:survey_id>/', views.result, name='result'),
    path('survey/<uuid:survey_id>/', views.survey, name='survey'),
    path('complete', views.complete, name='complete'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
]
