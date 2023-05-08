"""defines URL patterns for learning_logs app"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #home Page
    path('', views.index, name='index'),
    #page that shows topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # page for adding new topics
    path('new_topic/', views.new_topic, name='new_topic'),
    #page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #page for delting an entry
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    #page for deleting a topic
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]