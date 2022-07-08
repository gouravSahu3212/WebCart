from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request,"blog/login.html")

def stream(request):
    # return render(request,"blog/stream.py")
    os.system('cmd /k "streamlit run stream.py"')
    return 0