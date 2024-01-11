from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

# books = [
#     {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian', 'description': 'A novel about a totalitarian regime that uses surveillance and propaganda to control its citizens.', 'published_year': 1949},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Southern Gothic', 'description': 'A story of racial injustice and the destruction of innocence, set in the Deep South.', 'published_year': 1960},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Dystopian', 'description': 'A futuristic society driven by technological and genetic advancements, with disturbing undercurrents.', 'published_year': 1932},
#     {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Tragedy', 'description': 'An exploration of the American Dream and its discontents in the Roaring Twenties.', 'published_year': 1925}
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books
    })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', { 
        'book': book
    })


class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
  model = Book
  fields = '__all__'

class BookDelete(DeleteView):
  model = Book
  success_url = '/books'