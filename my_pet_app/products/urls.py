from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('products/', views.products, name='products'),
    path('products/<int:pk>/', views.product_details, name='product_details'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('testing/', views.testing, name='testing'),
]