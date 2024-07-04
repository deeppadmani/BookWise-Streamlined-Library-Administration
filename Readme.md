#  BookWise-Streamlined-Library-Administration
The BookWise-Streamlined-Library-Administration is a comprehensive software solution designed to streamline library operations, including book search, loan management, borrower management, and fine generation. It features a user-friendly Graphical User Interface (GUI) built using Django, a powerful web framework known for its efficiency and practical design approach.
## Features
### 1. Graphical User Interface (GUI)
- Developed using Django for efficient development and a clean interface.
- Utilizes Django's Object Relational Mapper (ORM) for seamless communication between the database and models, reducing errors and simplifying operations.
### 2. Book Search and Availability
- Books are uniquely identified by ISBN10 codes in the database.
- Book details include title, ISBN10, authors, and availability status.
- Search by ISBN10 or author's name with error handling for partial matches and book availability.
- Ability to loan books directly from search results.
### 3. Book Loans
- Facilitates book loans with user-friendly forms for checking out and checking in books.
- Error handling for invalid card IDs, maximum loan limits, unavailable books, and outstanding fines.
- Automation for loan dates and ID generation.
### 4. Borrower Management
- Manage borrower records with automatic generation of Card IDs.
- Mandatory fields for SSN, name, and address with error handling for duplicate SSNs, incomplete fields, and invalid phone numbers.
- 
# Installation Process
```sh
install vscode
install python3.11.5 
install mysql Ver 8.0.34 for Win64 on x86_64 (MySQL Community Server - GPL) 
install pip 
install virtualenv
pip3 install virtualenv
```
Copy my Project Folder BookWise-Streamlined-Library-Administration to your preferred directory
Open a command prompt in your system and Go to directory BookWise-Streamlined-Library-Administration eg
```sh
cd C:\Users\deepp\OneDrive\Desktop\BookWise-Streamlined-Library-Administration
```
Open the BookWise-Streamlined-Library-Administration in vsCode and edit the following
```sh
Open Folder myDJango\my_Django: open settings.py file and add 'LibraryManagementSystem'
INSTALLED_APPS = [ 'django.contrib.admin', 
                  'django.contrib.auth',   
                  'django.contrib.contenttypes', 
                  'django.contrib.sessions', 
                  'django.contrib.messages', 
                  'django.contrib.staticfiles', 
                  'LibraryManagementSystem', ]
```

Update the database and User Password
```sh
DATABASES = { 'default': { 
                'ENGINE': 'django.db.backends.mysql', 
                'NAME': 'library', 
                'USER': 'root', 
                'PASSWORD': 'YOUR_DB_PASSWORD', #change for your Database 
                'HOST':'localhost', 
                'PORT':'3306', } }
```
Create virtual environment
```sh
python3 -m venv venv
```

Activate the virtual environment
```sh
venv\Scripts\activate
```
In the virtual environment execute the following command
```sh
pip install django
pip install mysql
pip install mysql-connector 
pip install mysql-connector-python 
pip install mysqlclient
pip install pandas
```
Now Open BookWise-Streamlined-Library-Administration\myDJango\my_Django and run 
```sh
python CreateDataBase.py #Creates a Schema in mysql named BookList. You can check it in your mysql
python manage.py makemigrations
python manage.py migrate
```
Run the CreateDataBaseFromCSV.py file to fill the data in tables
```sh
python CreateDataBaseFromCSV.py     #Create Database from csv file
```
After it is done, you do
```sh
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```
copy the server address to a browser
```sh
http://127.0.0.1:8000/
```
