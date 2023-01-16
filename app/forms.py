from django.forms import ModelForm
from .models import Book, Customer, Loan

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CustForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'