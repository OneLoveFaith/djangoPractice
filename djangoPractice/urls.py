"""
URL configuration for djangoPractice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from book.views import BookListView, BookDetailView, AddBookView, DeleteBookView, EditBookView, SearchBookView, \
    DeleteCommentView

from clothes.views import OrderCreateView, ProductListView, OrderListView, \
    OrderDetailView, OrderDeleteView, ProductFilterView, ProductCreateView, AddTagView, ProductDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('delete_book/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
    path('edit/<int:pk>/', EditBookView.as_view(), name='edit_book'),
    path('search/', SearchBookView.as_view(), name='search_book'),
    path('book/<int:book_id>/comment/<int:comment_id>/delete/', DeleteCommentView.as_view(), name='delete_comment'),

    path('add_tag/', AddTagView.as_view(), name='add_tag'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('products/filter/<int:tag_id>/', ProductFilterView.as_view(), name='product_list_by_tag'),

    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)