from django.urls import path
from . import views

app_name = 'Book_store'

urlpatterns = [
	path('', views.showBooks, name = 'store-home'),
	path('about/', views.about, name = 'store-about'),
	path('booklist/',views.booklist, name ='store-booklist'),
	path('contact/',views.contact,name='store-contact'),
	path('booklist/<int:book_id>/',views.description,name='store-description'),
	path('results/', views.search, name='search'),
]