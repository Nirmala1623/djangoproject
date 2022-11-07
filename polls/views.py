from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def student_details(request):
    return render(request,'home.html',{'name':'Nirmala'})