from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Book, Comment
from .forms import CommentForm, BookForm
from django.urls import reverse_lazy
from django.db.models import Count

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return super().get_queryset().annotate(num_comments=Count('comments'))

class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/add_book.html'
    success_url = reverse_lazy('book_list')

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'book/book_detail.html'
    success_url = reverse_lazy('book_list')

class EditBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/edit_book.html'

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.pk})

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(book=self.object)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = self.get_object()
            comment.save()
        return self.get(request, *args, **kwargs)



class DeleteCommentView(View):
    def post(self, request, book_id, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        return redirect('book_detail', pk=book_id)

class SearchBookView(View):
    template_name = 'book/search_results.html'

    def get(self, request):
        query = request.GET.get('q')
        if query:
            books = Book.objects.filter(title__icontains=query)
        else:
            books = []

        return render(request, self.template_name, {'books': books, 'query': query})