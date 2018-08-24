# lib/view.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
def index(request):
    return HttpResponse("Hello, world")

def detail(request):
    book_list = Book.object.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'lib/detail.html',context)
# Create your views here.
