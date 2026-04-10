from django.urls import path
from . import views

urlpatterns = [
    # 🔹 메인 - 주제 목록
    path('', views.topic_list, name='topic_list'),

    # 🔥 투표 생성 (먼저 선언)
    path('topic/create/', views.topic_create, name='topic_create'),

    # 🔹 주제 상세
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),

    # 🔹 투표 처리
    path('vote/<int:project_id>/', views.vote, name='vote'),

    # 🔹 결과 페이지
    path('result/<int:topic_id>/', views.result, name='result'),

    # 🔹 투표 초기화
    path('reset/<int:topic_id>/', views.reset_votes, name='reset_votes'),

    # 🔥 주제 삭제
    path('topic/delete/<int:topic_id>/', views.topic_delete, name='topic_delete'),
]