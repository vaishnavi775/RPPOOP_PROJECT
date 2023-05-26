from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# importing pandas as pd and csv
import pandas as pd
import csv
from django.contrib.auth.models import User
from .models import validate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.shortcuts import render
import streamlit as st

def streamlit_view(request):
    return render(request, 'streamlit_app.html')


# Read the Excel file into a Pandas DataFrame.
# df = pd.read_excel("static\PSF'23.xlsx")

# Create a list of the columns you want to add from Excel.
# columns_to_add = ["Student Name", "MIS No"]

# Use the `loc` method to select the rows and columns you want to add.
# df = df.loc[:, columns_to_add]

# Write the DataFrame to a CSV file.
# df.to_csv('fest.csv', index=False)


# df = pd.read_csv('fest.csv')
# ##removes space from strings  
# def remove(string):
#     return string.replace(" ", "")
# df['username'] = df['Student Name'].apply(remove)       #creates new column named username 
# df.drop('Student Name', axis=1, inplace=True)           ##removes the old column
# df['password'] = df['MIS No']
# df.drop('MIS No', axis=1, inplace=True)
# df.to_csv('fest.csv', index=False)

#creating users
# import csv
# from django.contrib.auth.models import User

# with open('fest.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         username = row['username']
#         password = row['password']
#         user = User.objects.create_user(username=username, password=password)
#         user.save()

#superuser manager pw manager
# @login_required
def home(request):
    # users = validate.objects.
    return render(request, 'authenticate/home.html')


# def login_user(request):
#     # if request.user.is_authenticated:
#     #     return redirect("/")
#     # else:
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             user = validate.objects.get(username=username, password=password)
#             # Perform login operation if user exists
#             messages.success(request, ('You Have Been Logged In!'))
#             return redirect('home')  # Replace 'home' with your desired URL name for the home page
#         except validate.DoesNotExist:
#             # Handle invalid login credentials
#             error_message = 'Invalid username or password.'
#             return render(request, 'authenticate/login.html', {'error': 'Invalid username or password.'})
#     return render(request, 'authenticate/login.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = validate.objects.get(username=username, password=password)
            # Perform login operation if user exists
            messages.success(request, ('You Have Been Logged In!'))
            # return redirect('home')  # Replace 'home' with your desired URL name for the home page
            return redirect('http://localhost:8501')  # Replace 'home' with your desired URL name for the home page
        except validate.DoesNotExist:
            # Handle invalid login credentials
            error_message = 'Invalid username or password.'
            return render(request, 'authenticate/login.html', {'error_message': error_message})
    return render(request, 'authenticate/login.html')



def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out...'))
    return redirect('home')

    