from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
