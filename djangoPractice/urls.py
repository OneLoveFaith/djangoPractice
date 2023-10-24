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
from book import views
from book.views import book_list, book_detail

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)