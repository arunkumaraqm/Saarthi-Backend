from django.conf.urls import url
from django.urls import path
from ice import views

urlpatterns = [
	path('external-books', views.get_book),
	path('v1/books', views.books),
	path('v1/books/<int:id>', views.get_book_by_id),
	path('v1/books/<int:id>/update', views.get_book_by_id),
]