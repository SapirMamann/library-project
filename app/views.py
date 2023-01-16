from .models import Customer, Book, Loan
from .forms import BookForm, CustForm, LoanForm

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def index(request):
    """ 
    home page
    """
    books = Book.objects.all()
    book_count = books.count()
    context = {'msg': 'main page','books': books, 'book_count': book_count}
    return render(request, 'app/index.html', context)


def login_page(request):
    page = 'login'  #app/login
    # return render(request, 'app/login_register_page.html', {'msg': 'msg'})
    if request.user.is_authenticated:                         #a logged in user cant get to the log in page
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()                         #take the parameters the user entered
        password = request.POST.get('password')
        try:                            #check if this user exists(he registered before) 
            user = User.objects.get(username=username, password=password)
        except:                         #this user hasnt registered yet
            messages.error(request, "User does not exist")
            # return HttpResponse('user does not existttttttttt')   #<<<<<<<
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:                            #log the known user in
            login(request, user)
            return redirect('index')                            #and go straight to the main page
        else:
            return HttpResponse('user/password does not exist')                         #unregisterd user tried to sign in
        
                              #get method
        # form = UserCreationForm
        # return render(request, 'app/login.html', {'form': form})
        
    context = {'page': page}
    return render(request, 'app/login_register.html', context)
        
      
def logout_page(request):
    logout(request)
    return redirect('index')


def register_page(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()   #<< commit false
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('an error occured during registeration')
    
    context = {'form': form}
    return render(request, 'app/login_register.html', context)
        
        
def add_book(request):
    """ 
    add a new book
    """
    form = BookForm()
    """books = books.objects.all -> then i can check if book already exists"""
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)  # <<<<<<< i forgot what commit means
            book.save()
            return redirect('books-list')
        
    context = {'form': form}
    return render(request, 'app/book_form.html', context)


def books_list(request):
    """ 
    show all books
    """
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'app/books_list.html', context)


def book_detail(request, pk):
    """
    view details of a specific book
    """
    book = Book.objects.get(id=pk)
    context = {'book': book}
    return render (request, 'app/book_detail.html', context)


def add_cust(request):
    """
    add a new customer
    """
    form = CustForm()
    
    if request.method == "POST":
        form = CustForm()
        
        Customer.objects.create(
            name = request.POST.get('name'),
            address = request.POST.get('address'),
            age = request.POST.get('age'),
        )
        return redirect('custs-list')
    
    context = {'form': form}
    return render(request, 'app/cust_form.html', context)

def cust_list(request):
    """ 
    show all customers
    """
    custs = Customer.objects.all()
    
    context = {'custs': custs}
    return render(request, 'app/custs_list.html', context)
    
    
def cust_detail(request, pk):
    """ 
    shows details of a specific customer
    """
    cust = Customer.objects.get(id=pk)
    
    context = {'cust': cust}
    return render(request, 'app/cust_detail.html', context)

def add_loan(request):
    """
    create a new loan
    """
    form = LoanForm()
    
    if request.method == "POST":
        # if form.is_valid():
            form = LoanForm
            book_id = request.POST['book']
            cust_name = request.POST['customer']
            Loan.objects.create(
                book = Book.objects.get(id=int(book_id)),
                customer = Customer.objects.get(id=int(cust_name)),
                # loan_date  and return date doesnt really matter i just need to make sure it automatically calculate the return date
            )
            return redirect('loans-list')
        
    context = {'form': form}
    return render(request, 'app/loan_form.html', context)
    

def loans_list(request):
    """
    show all loans
    """
    loans = Loan.objects.all()
    context = {'loans': loans}
    # context = {}
    return render(request, 'app/loans_list.html', context)

def loan_detail(request, pk):
    """
    show details of a specific loan
    """
    loan = Loan.objects.get(pk=pk)
    context ={'loan': loan}
    return render(request, 'app/loan_detail.html',context)