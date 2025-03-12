from django.http.response import HttpResponse

def education(request):
    return HttpResponse("Hi,you can choose your topic for your education.")

def education_topic(request, topic):
    return HttpResponse(f"This page is for {topic} education.")
