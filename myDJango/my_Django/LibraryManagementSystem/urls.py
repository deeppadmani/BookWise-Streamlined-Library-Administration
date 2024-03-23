
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search_book',views.search_book,name='search-book'),
    path('book_loan',views.book_loan,name='book-loan'),
    path('add_borrower',views.add_borrower,name='add-borrower'),
    path('search_fines',views.search_fines,name='search-fines'),
    path('book_return',views.book_return,name='book-return'),
    path('navbar',views.navbar,name='nav-bar'),
]
