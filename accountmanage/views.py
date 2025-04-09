from django.http.response import HttpResponse
from accountmanage.models import Customer, Purchase
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        name = data.get("name"),
        password = data.get("password"),

        customer = Customer.objects.filter(name = name).first()

        if customer is None:
            return HttpResponse("the user was not found.")
        
        if customer.password != password:
            return HttpResponse("Your password is incorrect.")
        
        return HttpResponse(f"welcome {name}")

    return HttpResponse ("please enter your name and password")

@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Customer.objects.create(
            name = data.get("name"),
            password = data.get("password"),
            phone = data.get("phone"),
            email = data.get("email"),
        )
        return HttpResponse("user created")


       


