from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.IndexView.as_view(), name='home'),
	path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
    path('my-post/', views.MyView.as_view(), name="myview"),
    path('create/', views.NewBlatView.as_view(), name="newblat"),
    path('post/<int:pk>/edit/',
        views.EditBlatView.as_view(), name='editblat'),
    path('user', views.TemplateViews.as_view(), name ='user_info'),
    path('post/<int:pk>/delete/',
      views.BlogDeleteView.as_view(), name='delete'),
    
]