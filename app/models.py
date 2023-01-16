from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author = models.CharField(max_length=45)
    genre = models.CharField(max_length=45)
    # published_year = models.DateTimeField()
    copies = models.PositiveIntegerField(default=1)
    
    class meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=1)
    # books_loaned = models.ForeignKey()
    
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(auto_now=True)
    # returned = models.BooleanField()

    def __str__(self):
        return self.book