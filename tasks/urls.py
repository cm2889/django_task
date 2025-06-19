from django.urls import path
from . import views

# Create your views here.
app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='password_change'),
   
]
