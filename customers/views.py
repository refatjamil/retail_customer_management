from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

# Implement other views for creating, updating, and deleting customers
