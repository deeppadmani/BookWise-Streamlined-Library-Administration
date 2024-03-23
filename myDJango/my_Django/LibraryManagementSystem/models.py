
from django.db import models
from django.utils import timezone

class Book(models.Model):
    ISBN10 = models.CharField(max_length=10,primary_key=True)
    Title = models.CharField(max_length=200)
    Available = models.BooleanField(default = True)
    
    def __str__(self):
        return f"data : {self.ISBN10},{self.Title}"
    

class Authors(models.Model):
    AuthorId = models.AutoField(primary_key=True,default=1)
    Name = models.CharField(max_length=255,default='',unique=True)
    
    def __str__(self):
        return f"Authors: {self.Name}"
    

class BookAuthors(models.Model):
    AuthorId = models.ForeignKey(Authors, related_name="Auth", on_delete=models.CASCADE)
    ISBN10 = models.ForeignKey(Book,related_name='ISBN10_authors', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"BookAuthors : {self.AuthorId},{self.ISBN10}"
        
class Borrower(models.Model):
    CardId = models.CharField(max_length=8,primary_key=True)
    SSN = models.CharField(max_length=12,unique=True)
    Bname = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    State = models.CharField(max_length=2)
    Phone = models.CharField(max_length=14)

    def __str__(self):
        return f"Borrower : {self.CardId},{self.SSN},{self.Bname},{self.Address},{self.Phone}"
    
class BookLoans(models.Model):
    LoanId = models.AutoField(primary_key=True)
    ISBN10 = models.ForeignKey(Book,related_name='ISBN10_BookLoans', on_delete=models.CASCADE)
    CardId = models.ForeignKey(Borrower,related_name='CardId_BookLoans', on_delete=models.CASCADE)
    Date_out = models.DateField(timezone.now)
    Due_Date = models.DateField(default=timezone.now() + timezone.timedelta(days=14))
    Date_in = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"BookLoans : {self.LoanId},{self.ISBN10},{self.CardId},{self.Date_out},{self.Due_Date},{self.Date_in}"
    


class Fines(models.Model):
    LoanId = models.ForeignKey(BookLoans,related_name='LoanId_Fines',on_delete=models.CASCADE)
    Fine_amt = models.DecimalField(max_digits=10, decimal_places=2)
    Paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fines : {self.LoanId},{self.Fine_amt},{self.Paid}"