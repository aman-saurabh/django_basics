from django.shortcuts import render, redirect

# Create your views here.
from database_app.models import Order
from django.core import serializers
import json

def order(request):
    data = serializers.serialize("json", Order.objects.all(), fields=('customer_name', 'total_items', 'price'))
    print(data)
    return render(request, 'template_order_form.html')
    '''
    It will produce result in the following manner
    [{"model": "database_app.order", "pk": 1, 
    "fields": {"customer_name": "Aman", "total_items": 5, "price": 15000}}, ...]
    i.e actual data is represented by "fields" property and primary key value(i.e 'id') by "pk" property
    And it returns only 'customer_name', 'total_items' and 'price' because we have specified it in the query 
    (i.e in serializers.serialize method) using "fields" property
    '''


def add_order(request):
    data = {
        "customer_name": request.POST.get('customer_name'),
        "address": request.POST.get('address'),
        "total_items": int(request.POST.get('item')),
        "price": int(request.POST.get('price')),
        "is_delivered": True if request.POST.get('is_delivered') == 'delivered' else False
    }
    print(data)
    # current_order = Order(customer_name=data.get('customer_name'), address=data.get('address'),
    #                       total_items=data.get('total_items'), price=data.get('price'), is_delivered=data.get('is_delivered'))
    # current_order.save()

    formatted_data = [{"model": "database_app.order", "pk": 1, "fields": data}]
    json_formatted_data = json.dumps(formatted_data)
    for deserialized_object in serializers.deserialize("json", json_formatted_data):
        # obj = deserialized_object.object
        # print(obj)
        deserialized_object.save()
    return redirect('/order')
