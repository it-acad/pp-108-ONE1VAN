# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from author.models import Author
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookForm


def books_view(request):
    title_filter = request.GET.get('title', '')
    author_filter = request.GET.get('author', '')
    
    books = Book.objects.all()
    
    if title_filter:
        books = books.filter(name__icontains=title_filter)  
    
    if author_filter:
        books = books.filter(authors__id=author_filter)  

    authors = Author.objects.all()
    return render(request, 'book/books_view.html', {'books': books, 'authors': authors})

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("The book was not found")
    return render(request, 'book/book_detail.html', {'book': book})

@login_required
def create_book(request):
    if request.user.role != 1:  
        return redirect('home')

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('view')  
    else:
        form = BookForm()

    return render(request, 'book/create_book.html', {'form': form})

