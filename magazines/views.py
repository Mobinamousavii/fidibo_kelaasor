from django.http.response import HttpResponse

def magazines(request):
    return HttpResponse("Hi,you can choose your topic for your magazines.")

def magazines_topic(request, topic):
    return HttpResponse(f"This page is for {topic} magazines.")

