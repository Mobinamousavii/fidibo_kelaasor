from django.contrib.admin import ModelAdmin, register
from accountmanage.models import Purchase, Customer

@register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ['name', 'phone']

class PurchaseAdmin(ModelAdmin):
    list_display = ['customer', 'book']


