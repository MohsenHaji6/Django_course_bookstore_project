from django.views import generic
from django.urls import reverse

from .models import Book

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'price',]
    template_name = 'books/book_create.html'

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'price',]
    template_name = 'books/book_update.html'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.pk})
