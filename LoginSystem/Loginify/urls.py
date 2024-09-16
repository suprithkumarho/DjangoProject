from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home,name='home'), 
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),

    path('users/', views.get_all_users,name='all_users'),
    path('user/<str:email>/', views.get_user_by_email,name='user_detail'),
    path('update/<str:username>/', views.update_user,name='update_user'),
    path('delete/<str:email>/', views.delete_user,name='delete_user'),
]
