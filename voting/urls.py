from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('vote/<int:project_id>/', views.vote, name='vote'),
    path('result/<int:topic_id>/', views.result, name='result'),
    path('reset/<int:topic_id>/', views.reset_votes, name='reset_votes'),
]