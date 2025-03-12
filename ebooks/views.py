from django.http.response import HttpResponse

def ebooks(request):
    return HttpResponse("Hi,you can choose your topic for your ebooks.")

def ebook_topic(request, topic):
    return HttpResponse(f"This page is for {topic} ebooks.")