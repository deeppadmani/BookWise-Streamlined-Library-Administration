#Installation Process

#install vscode # Program Editor
#install python3.11.5 
#install mysql Ver 8.0.34 for Win64 on x86_64 (MySQL Community Server - GPL)
#install pip
#install virtualenv    

pip3 install virtualenv

#Copy my Project Folder DMP210005_DatabaseProject to your preferred directory 

#Open a command prompt in your system and Go to directory DMP210005_DatabaseProject eg:  C:\Users\deepp\OneDrive\Desktop\DMP210005_DatabaseProject

#Open the DMP210005_DatabaseProject folder in vsCode and edit the following 

#Under Folder myDJango\my_Django: open settings.py file 
#Check under INSTALLED_APPS if 'LibraryManagementSystem' is added
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'LibraryManagementSystem',
]

#update the database and User Password
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library',
        'USER': 'root',
        'PASSWORD': 'Deep@1313',	#change for your Database 
        'HOST':'localhost',
        'PORT':'3306',
    }
}


#Changes in CreateDataBase.py and CreateDataBaseFromCSV.py
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Deep@1313'	#change according to your MySql database
)


# Go to directory DMP210005_DatabaseProject and Create virtual environment
python3 -m venv venv

#Activate the virtual environment
env\Scripts\activate 

#In the virtual environment execute the following command

#install Django
pip install django 


#install mysql 
pip install mysql 

#install connectors 
pip install mysql-connector
pip install mysql-connector-python
pip install mysqlclient

#install python library
pip install pandas

#Go to directory DMP210005_DatabaseProject\myDJango\my_Django run the CreateDataBase.py file 
python CreateDataBase.py           #Creates a Schema in mysql named BookList. You can check it in your mysql  

#make migrations 
python manage.py makemigrations
python manage.py migrate 

#run the CreateDataBaseFromCSV.py file to fill the data in tables
python CreateDataBaseFromCSV.py		#Create Database from csv file 

#After it is done, Again make migrations 
python manage.py makemigrations
python manage.py migrate
		
#runserver
python manage.py runserver


#copy the server address to a browser
http://127.0.0.1:8000/





