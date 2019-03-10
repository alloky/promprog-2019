from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_questions, name='all_questions'),
    path('questions', views.all_questions, name='all_questions'),
 	path('new_question', views.new_question, name='new_question'),
 	path('add_question', views.add_question, name='new_question'),

]