from django.forms import ModelForm
from django import forms
from .models import Book, Customer
from django.contrib.auth.models import User
from django.forms import ValidationError

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CustForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


#
# Functions for data validations in authentication
#
def validate_username(val: int):
    if not val.isalnum():
        raise ValidationError('The Username field cannot conain any special characters.')
    if val.isnumeric():
        raise ValidationError('The Username field cannot only contain numbers.')
    

def validate_password(val: int):
    if len(val) > 32:
        raise ValidationError('The Password field may only be up to 32 characters.')
    

def validate_age(val: int):
    if type(val) != int:
        raise ValidationError(f'The age field must be a number.')
    
    if val < 0:
        raise ValidationError(f'The age field cannot be negetive.')
    elif val == 0:
        raise ValidationError(f'The age field cannot be zero.')
    elif (5 > val) or (val > 120):
        raise ValidationError(f'The age field can only be a number between 5 and 120 years old.')

class LoginForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    password = forms.CharField(label='Your password', max_length=100, widget=forms.PasswordInput())

    class Meta:
        model = User
        field = ['username', 'password']


class RegisterForm(forms.Form):
    username  =  forms.CharField(    label='Your username',         max_length=100, validators=[validate_username])
    password  =  forms.CharField(    label='Your password',         max_length=100, validators=[validate_password], widget=forms.PasswordInput())
    email     =  forms.EmailField(   label='Your Email Address',    max_length=100)
    age       =  forms.IntegerField( label='Your age', min_value=5, max_value=120,  validators=[validate_age]) # Added 'min_value' and 'max_value' attributes for idiot-proof validation

    class Meta:
        model = User
        field = ['username', 'password', 'email', 'age']