from django import forms
from LibraryManagementSystem.models import Book , Authors, BookAuthors, Borrower, BookLoans


class SearchedBookList:
    def __init__(self,isbn10,bookTitles,authors,Available) :
        self.isbn10 = isbn10
        self.bookTitles = bookTitles
        self.authors = authors
        self.Available = Available

    def __str__(self):
        return f"SearchedBookList : {self.isbn10},{self.bookTitles},{self.authors},{self.Available}"

class SearchedFineList:
    def __init__(self,CardId,TotalFine,Paid) :
        self.CardId = CardId
        self.TotalFine = TotalFine
        self.Paid = Paid

