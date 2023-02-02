from django.urls import path

from . import views

# app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    
    path('add_book/', views.add_book, name='add_book'),
    path('books/', views.books_list, name ='books_list'),
    path('book/<str:pk>/', views.book_detail, name='book_details'),

    path('add_cust/', views.add_cust, name='add_customer'),
    path('customers/', views.cust_list, name='customers_list'),
    path('customer/<str:pk/', views.cust_detail, name='customer_details'),
    
    path('add_loan/', views.add_loan, name='add_loan'),
    path('loans/', views.loans_list, name='loans_list'),
    path('loan/<str:pk/', views.loan_details, name='loan_details'),
    

]