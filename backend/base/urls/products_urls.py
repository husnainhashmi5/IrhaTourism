from django.urls import path,include

from base.views import products_views as views
urlpatterns=[
   
    path('', views.getrPoducts,name='products'),
    path('<str:pk>/', views.getProduct,name='product')
]