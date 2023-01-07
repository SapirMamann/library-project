from django.forms import ModelForm
from .models import Book, Customer

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CustForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'