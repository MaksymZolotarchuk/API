from django.shortcuts import render, redirect, get_object_or_404
from .form import CustomerForm
from .models import Customer
from .NetworkHelper import NetworkHelper

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = "max"
PASSWORD = "123"

def customer_list(request):
    network_helper = NetworkHelper(BASE_URL, USERNAME, PASSWORD)
    customers = network_helper.get_items()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_detail(request, id):
    network_helper = NetworkHelper(BASE_URL, USERNAME, PASSWORD)
    customer = network_helper.get_item_by_id(id)
    return render(request, 'customer_detail.html', {'customer': customer})

def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            network_helper = NetworkHelper(BASE_URL, USERNAME, PASSWORD)
            form_data = form.cleaned_data
            network_helper.create_item(form_data)
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer_delete_confirmation.html', {'customer': customer})

def customer_edit(request, id):
    customer = Customer.objects.filter(id=id)
    #customer = get_object_or_404(Customer, pk=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form, 'edit': True})
