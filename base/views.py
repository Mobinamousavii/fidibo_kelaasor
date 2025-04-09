from django.http.response import HttpResponse , JsonResponse
from accountmanage.models import Customer, Purchase
from base.models import Book
from ebooks.models import Ebooks
from audiobooks.models import Audio_books
from education.models import Education_books
from magazines.models import Magazines
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def ebook_list(request):
    ebooks = Ebooks.objects.all().order_by("title").values("title", "author", "price", "id")
    ebooks = list(ebooks)
    return JsonResponse(ebooks, safe=False)   

def audiobook_list(request):
    audiobooks = Audio_books.objects.all().order_by("title").values("title", "author", "price", "id")
    return JsonResponse(list(audiobooks), safe=False)

def educationbook_list(request):
    education_books = Education_books.objects.all().order_by("title").values("title", "author", "price", "id")
    return JsonResponse(list(education_books), safe=False)

def magazine_list(request):
    magazines = Magazines.objects.all().order_by("title").values("title", "author", "price", "id")
    return JsonResponse(list(magazines), safe=False)

@login_required
def purchasing(request, book_id):
     if request.method == "POST":
        customer = request.user.customer
        book = get_object_or_404(Book, id=book_id)

        if not Purchase.objects.filter(customer=customer, book=book).exists():
            Purchase.objects.create(customer=customer, book=book)
            return JsonResponse({"purchased completed succssfully."})
        else:
            return JsonResponse({"you have already purchased this book."})

     return JsonResponse({"error": "Only POST requests are allowed"}, status=405)