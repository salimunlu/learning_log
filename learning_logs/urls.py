from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),  # Bütün konuların sayfası
    path('topics/<int:topic_id>/', views.topic, name='topic'), # Konuların ayrı sayfaları
    path('new_topic/', views.new_topic, name='new_topic'), # Yeni konu eklemek için
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), # Yeni entry eklemek için
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), # Entry düzenlemek için
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'), # Entry silmek için
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'), # Topic silmek için
    path('about/', views.about, name='about'),
]
