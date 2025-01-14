from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order
from django.utils import timezone

@login_required
def create_order(request):
    if request.user.role == 1:
        return redirect('home')  

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_success')  
    else:
        form = OrderForm()

    return render(request, 'order/create_order.html', {'form': form})
def order_success(request):
    return render(request, 'order/order_success.html')

@login_required
def all_orders(request):
    if request.user.role != 1: 
        return redirect('home')

    orders = Order.objects.all()  
    return render(request, 'order/all_orders.html', {'orders': orders})

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/user_orders.html', {'orders': orders})

