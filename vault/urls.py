from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Password features
    path('add/', views.add_password, name='add_password'),
    path('update/<int:pk>/', views.update_password, name='update_password'),
    path('delete/<int:pk>/', views.delete_password, name='delete_password'),
    path('search/', views.search_password, name='search_password'),
]