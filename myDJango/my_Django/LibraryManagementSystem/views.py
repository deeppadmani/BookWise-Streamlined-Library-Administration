from django.shortcuts import render
from LibraryManagementSystem.models import Book , Authors, BookAuthors, Borrower, BookLoans,Fines
from django.db.models import Q
from LibraryManagementSystem.form import SearchedBookList ,SearchedFineList
from django.db.models import Sum
from django.http import HttpResponseRedirect
import random
from django.utils import timezone

def home(request):
    return render(request,'home.html',{})
            
def search_book(request):
    if request.method == "POST":
        searchedbook = request.POST['searchedbook']
        ReaultSearchedBook = Book.objects.filter(Q(Title__icontains = searchedbook) | Q(ISBN10__icontains = searchedbook))
        SearchedBookListobj =[]
        if not searchedbook:
            return HttpResponseRedirect("/")
        for book in ReaultSearchedBook:
            Authoers = BookAuthors.objects.filter(ISBN10 = book.ISBN10).values_list('AuthorId__Name',flat=True)
            Authname = ', '.join(Authoers)
            SearchedBookListobj.append(SearchedBookList(book.ISBN10,book.Title ,Authname,book.Available))

        ReaultSearchedBook = BookAuthors.objects.filter(AuthorId__Name__icontains=searchedbook).values(
                'ISBN10',
                'ISBN10__Title',
                'AuthorId__Name',
                'ISBN10__Available' )
        
        for book in ReaultSearchedBook:
            SearchedBookListobj.append(SearchedBookList(book['ISBN10'], book['ISBN10__Title'] , book['AuthorId__Name'], book['ISBN10__Available']))

        return render(request,
                  'base.html',
                  {'searchedbook':searchedbook,
                   'SearchedBookListobj':SearchedBookListobj})
    else: 
        return HttpResponseRedirect("/")
    

    
def book_loan(request):
    submitted = request.GET.get('submitted',False)
    ISBN = request.GET.get('isbn')
    errorVar = False
    borrower = None
    totalbook = None
    messages = {'msgInputISBN': '', 'msgInputCardID': '', 'msgInputDateIN': '', 'msgInputDueDate': '','msgSubmit': '','error':''}
    if request.method == 'POST':
        PostISBN = request.POST.get('inputISBN','')
        PostCardID = request.POST.get('inputCardID','')
        PostDateIN = request.POST.get('inputDateIN','')
        PostDueDate = request.POST.get('inputDueDate','')

        book = Book.objects.get(ISBN10 = PostISBN)
        
        if Borrower.objects.filter(CardId = PostCardID).exists():
            borrower = Borrower.objects.get(CardId = PostCardID)
            BookLoanObj = BookLoans(ISBN10=book,CardId=borrower,Date_out=PostDateIN,Due_Date=PostDueDate)
            totalbook = BookLoans.objects.filter(CardId = PostCardID,  Date_in__isnull=True).count()
        else:
            messages['msgInputCardID'] = 'Card-ID dose not exists'
            errorVar = True

        if Fines.objects.filter(LoanId__CardId__CardId=PostCardID,Paid=False).exists():
                messages['error'] = 'Card Id has some Fines..!'
                errorVar = True

        if totalbook == 3:
            messages['msgInputCardID'] = 'Card ID has already 3 books'
            errorVar = True
        

        if book.Available == 0:
            messages['msgInputISBN'] = 'This Book is not available'
            errorVar = True
            
        if all([PostISBN, PostCardID, PostDateIN, PostDueDate]):
            try:
                if errorVar != True:
                    BookLoanObj.save()
                    book.Available = 0
                    book.save()
                    messages['msgSubmit'] = 'Data Saved Successfully!'
                    HttpResponseRedirect('/')
                
            except Exception as e:
                messages['error'] = f'Error: {e}'
                
    else:
        if 'submitted' in request.GET:
            submitted = True 
    
    return render(request,'book_loan.html',{'ISBN':ISBN, 'submitted':submitted,'messages':messages})

def add_borrower(request):
    messages =""
    if request.method == 'POST':
        PostSSN = request.POST.get('inputSSN','')
        PostFname = request.POST.get('inputFname','')
        PostLname = request.POST.get('inputLname','')
        PostAddr = request.POST.get('inputAddr','')
        PostCity = request.POST.get('inputCity','')
        PostState = request.POST.get('inputState','')
        PostPno = request.POST.get('inputPno','')
        PostBname = PostFname +" "+ PostLname
        PostCardID = ""

        if not PostSSN.isdigit() and not PostPno.isdigit():
            messages = "Please Enter Digits.."

        PostPno = f"{PostPno[:3]}-{PostPno[3:6]}-{PostPno[6:]}"
        if Borrower.objects.filter(SSN=PostSSN).exists():
            messages = "SSN already exists"
        
        while True:
            num = random.randrange(1, 10**6)
            num_with_zeros = '{:06}'.format(num)
            num_with_zeros = str(num).zfill(3)
            PostCardID = "ID" + num_with_zeros
            
            if Borrower.objects.filter(CardId=PostCardID).exists():
                continue
            else:
                break
        if messages == "":
            BorrowerObj = Borrower(CardId=PostCardID,SSN=PostSSN,Bname=PostBname,Address=PostAddr,City=PostCity,State=PostState,Phone=PostPno)
            BorrowerObj.save()
    return render(request,'add_borrower.html', {'messages':messages})

def search_fines(request):
    filter = request.POST.get('filter_on_paid','all')
    SeachedFine = None 
    messages = ""
    ReaultSearchedFines = None
    if request.method == "POST":
        SeachedFine = request.POST.get('searchedfines',None)  
        if 'select_paid' in request.POST:
            selectedCardID  = request.POST.get('select_paid',None)
            if selectedCardID:
                print(selectedCardID)
                nonReturnBook = BookLoans.objects.filter(CardId=selectedCardID, Date_in__isnull=True,Due_Date__lt=timezone.now().date()).exists()
                print(nonReturnBook)
                if not nonReturnBook:
                    Fines.objects.filter(LoanId__CardId__CardId = selectedCardID).update(Paid = True)
                else:
                    messages = "Book not Returned"
        
            

    if filter =='paid':
        ReaultSearchedFines = Fines.objects.filter(Paid=True).values('LoanId__CardId__CardId', 'Paid').annotate(total_amount=Sum('Fine_amt'))
    elif filter =='unpaid':
        ReaultSearchedFines = Fines.objects.filter(Paid=False).values('LoanId__CardId__CardId', 'Paid').annotate(total_amount=Sum('Fine_amt'))
    else:
        if SeachedFine:
            ReaultSearchedFines = Fines.objects.filter(LoanId__CardId__CardId=SeachedFine).values('LoanId__CardId__CardId', 'Paid').annotate(total_amount=Sum('Fine_amt'))
        else:
            ReaultSearchedFines = Fines.objects.values('LoanId__CardId__CardId','Paid').annotate(total_amount=Sum('Fine_amt'))
    return render(request,'search_fines.html', 
            {'ReaultSearchedFines':ReaultSearchedFines})

def book_return(request):
    searchedbook = ''
    bookLoanData = None
    if request.method == "POST":
        searchedbook = request.POST.get('searchedbook','')
        
        bookLoanData = BookLoans.objects.filter(Q(CardId__CardId__icontains=searchedbook)|
                                                    Q(ISBN10__ISBN10__icontains=searchedbook) |
                                                    Q(CardId__Bname__icontains=searchedbook),Date_in__isnull = True)
        if 'select_Return' in request.POST:
                selected_book_id = request.POST.get('select_Return', None)
                BookLoans.objects.filter(ISBN10=selected_book_id).update(Date_in = timezone.now().date())
                Book.objects.filter(ISBN10=selected_book_id).update(Available = True)
                
    return render(request,
                    'book_return.html',
                    {'searchedbook':searchedbook,
                    'bookLoanData':bookLoanData})
   
def navbar(request):
    fine = 0
    if request.method == "POST":
        if 'update' in request.POST:
            dataForUpdate = BookLoans.objects.filter(Date_in__isnull=True,Due_Date__lt=timezone.now().date())
            
        for entry in dataForUpdate:
            if(timezone.now().date() > entry.Due_Date):
                fineDays = (timezone.now().date() - entry.Due_Date)
                fine = (fineDays.days)*0.25
                print(fine)
            if Fines.objects.filter(LoanId = entry).exists():
                Fines.objects.filter(LoanId = entry).update(Fine_amt = fine)
            else:
                if fine != 0:
                    Fines.objects.create(LoanId = entry,Fine_amt = fine,Paid = False)
            
            
    return render(request,'home.html',{})