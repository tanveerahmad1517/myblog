from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.IndexView.as_view(), name='home'),
	path('blat/<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
    path('my/', views.MyView.as_view(), name="myview"),
    path('create/', views.NewBlatView.as_view(), name="newblat"),
    path('blat/<int:pk>/edit/',
        views.EditBlatView.as_view(), name='editblat'),
    
]