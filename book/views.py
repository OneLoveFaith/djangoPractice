from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Comment
from .forms import CommentForm
from django.db.models import Count

def book_list(request):
    books = Book.objects.annotate(num_comments=Count('comments'))
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    comments = Comment.objects.filter(book=book)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            form = CommentForm()

    else:
        form = CommentForm()

    return render(request, 'book/book_detail.html', {'book': book, 'comments': comments, 'form': form})

def delete_comment(request, book_id, comment_id):
    book = get_object_or_404(Book, pk=book_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        comment.delete()

    return redirect('book_detail', book_id=book_id)