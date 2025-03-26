from django.urls import path,include
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_confirmation, name='delete_confirmation'),
    # path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]