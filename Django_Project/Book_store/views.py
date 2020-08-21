from django.shortcuts import render
from django.core.mail import send_mail
from Django_Project import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from Book_store.models import Book



def search(request):
	search_term = ''
	search_results = ''
	books=''
	if 'search' in request.GET:
		search_term = request.GET['search']
		search_results = Book.objects.all().filter(id=search_term) 
	books = Book.objects.all()
	return render(request, 'search_result.html', {'books' : books, 'search_results': search_results })    
# Create your views here.
def description(request,book_id):
	book=get_object_or_404(Book, id=book_id)
	return render(request,"description.html", dict(book=book))
def about(request):
	return render(request, "about.html")

def booklist(request):
	books = Book.objects.all()
	return render(request,"booklist.html", {'books' : books})

# def sendmail(request):
# 	subject = "Order successfully palced"
# 	msg = "Your order from SOFTCOVER is on the way"
# 	to = "User."
# 	res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
# 	return render(request, "confirm.html")

def showBooks(request):
	return render(request, "home.html")
def contact(request):
	return render(request,"contact.html")