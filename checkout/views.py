from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M5s77EzA5UkcuSB6MyObD12bjiG3byCnEVy8PsHIvsdLXYXuQoGkhwr3kkxrH0h3Ds5JDH13HsAmN3ftv0DoJIY00O85Letbh',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
