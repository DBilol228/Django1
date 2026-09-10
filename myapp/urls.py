from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),

    path('categories/',views.categories,name='categories'),
    path('categories/<int:id>',views.category_detail,name='category_detail'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:id>/', views.category_detail, name='category_detail'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:id>/update/', views.update_category, name='update_category'),
    path('categories/<int:id>/delete/', views.delete_category, name='delete_category'),

    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:id>/update/', views.update_product, name='update_product'),
    path('products/<int:id>/delete/', views.delete_product, name='delete_product'),

    path('customers/', views.customers, name='customers'),
    path('customers/<int:id>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/<int:id>/update/', views.update_customer, name='update_customer'),
    path('customers/<int:id>/delete/', views.delete_customer, name='delete_customer'),
]
