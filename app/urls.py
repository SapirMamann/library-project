from django.urls import path

from . import views

# app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    
    path('add_book/', views.add_book, name='add-book'),
    path('books/', views.books_list, name = 'books-list'),
    path('book/<str:pk>/', views.book_detail, name='book-detail'),

    path('add_cust/', views.add_cust, name='add-cust'),
    path('customers/', views.cust_list, name='custs-list'),
    path('customer/<str:pk>/', views.cust_detail, name='cust-detail'),
    
    path('add_loan/', views.add_loan, name='add-loan'),
    path('loans/', views.loans_list, name='loans-list'),
    path('loan/<str:pk>/', views.loan_detail, name='loan-detail'),
    

]