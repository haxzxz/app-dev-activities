from django.urls import path
from . import views
from .views import register_view, CustomLoginView, CusstomLogoutView, profile_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.comment_add, name='comment_add'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CusstomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
]