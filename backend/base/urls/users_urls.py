from django.urls import path,include

from base.views import users_views as views
urlpatterns=[
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.RegisterUser,name='register-user'),
    path('profile/', views.getUserProfile,name='user-profile'),
    path('', views.getUsers,name='users'),

]