from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/task/', views.update_task, name='update_task'),
    path('delete/<int:pk>/task/', views.delete_task, name='delete_task'),
    path('search/task/', views.search_task, name='search_task'),
    path('task/<int:pk>/detail/', views.task_detail_view, name='task_detail_view'),
    
]

