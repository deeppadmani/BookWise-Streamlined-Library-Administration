import pandas as pd

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_Django.settings')
django.setup()

import mysql.connector
import re
from LibraryManagementSystem.models import Book , Authors, BookAuthors, Borrower
DataBaseName = "library"

dataBase = mysql.connector.connect(
    host = 'db',
    user = 'root',
    passwd = 'Deep@1313'
)

DBObj = dataBase.cursor()

DBObj.execute("USE " + DataBaseName)

AuthorId = 1 
print("Please Wait!! Reading CSV File...")
booktableprep = pd.read_csv('https://archive.org/download/books_202309/books.csv',sep='\t',engine='python') 
borrowerTablePrep = pd.read_csv('https://archive.org/download/borrowers_202309/borrowers.csv')
print("Please Wait!! Preparing DataBase...")

splitAuthro = [] 
for idx,raw in booktableprep.iterrows(): 
  bookTableObj = Book(booktableprep.ISBN10[idx],booktableprep.Title[idx])
  bookTableObj.save()
  del bookTableObj

  if pd.notna(booktableprep.Authro[idx]):
    if booktableprep.Authro[idx].__contains__(';') == True:
      splitAuthro = (booktableprep.Authro[idx]).replace(',',' ').split(';') #(r';',booktableprep.Authro[idx])
    else:
      splitAuthro = re.split(r',',booktableprep.Authro[idx])
    for authors in splitAuthro:
      authors = authors.lstrip()
      authors = authors.rstrip()
      if pd.notna(authors):
        AuthorTableObj = Authors(AuthorId = AuthorId,Name = authors)
        AuthorId +=1
      if Authors.objects.filter(Name=authors).exists() == False:
        AuthorTableObj.save()
        del AuthorTableObj
      
      Aid = Authors.objects.get(Name = authors)
      ISBN = Book.objects.get(ISBN10 = booktableprep.ISBN10[idx])

      Aid = Authors.objects.get(Name = authors)
      BookAuthorTableObj = BookAuthors(AuthorId = Aid,ISBN10 = ISBN)
      BookAuthorTableObj.save()
      del BookAuthorTableObj
      
    splitAuthro.clear()

BorrowerList = []
for idx,raw in borrowerTablePrep.iterrows():
    Name = borrowerTablePrep.first_name[idx] + " " + borrowerTablePrep.last_name[idx]
    borrowerTablePrep.ssn[idx] = borrowerTablePrep.ssn[idx].replace('-','')
    borrowerTablePrep.phone[idx] = borrowerTablePrep.phone[idx].replace('(','').replace(')',''.replace(' ','').replace('-',''))
    BorrowerObj = Borrower(borrowerTablePrep.ID0000id[idx],
                           borrowerTablePrep.ssn[idx],
                           Name,
                           borrowerTablePrep.address[idx],
                           borrowerTablePrep.city[idx],
                           borrowerTablePrep.state[idx],
                           borrowerTablePrep.phone[idx])
    BorrowerObj.save()
    del BorrowerObj
    
print("Done! Database is Ready!!")
