from django.http.response import HttpResponse

def audiobooks(request):
    return HttpResponse("Hi,you can choose your topic for your audiobooks.")

def audiobook_topic(request, topic):
    return HttpResponse(f"This page is for {topic} audiobooks.")




