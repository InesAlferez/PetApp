from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product
from .models import Contact
from .models import Cart


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart_item, created = Cart.objects.get_or_create(product=product, user=request.user)
        else:
            cart = request.session.get('cart', {})
            cart_item = cart.get(str(pk))
            if cart_item:
                cart_item['quantity'] += 1
            else:
                cart_item = {'quantity': 1, 'product_id': pk, 'product_name': product.name, 'product_price': product.price}
            cart[str(pk)] = cart_item
            request.session['cart'] = cart
        return redirect('add_to_cart', pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'cart.html', context)

def aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())

def cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
    else:
        cart = request.session.get('cart', {})
        cart_items = [{'product': cart_item['product_id'], 'quantity': cart_item['quantity']} for cart_item in cart.values()]
        total_price = sum(cart_item['quantity'] * Product.objects.get(pk=cart_item['product']).price for cart_item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

def contactus(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.message = request.POST.get('message')

        contact.name = name 
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
    return render(request, 'contactus.html')

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def products(request):
    myproducts = Product.objects.all().values()
    template = loader.get_template('all_products.html')
    context = {
        'myproducts': myproducts,
    }
    return HttpResponse(template.render(context, request))

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        cart_item, created = Cart.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('product_details', pk=pk)

    context = {
        'product': product,
    }
    return render(request, 'details.html', context)

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    cart_item.delete()
    return redirect('cart_view')

def testing(request):
    template = loader.get_template('testing.html')
    return HttpResponse(template.render(request))

def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            cart_item.quantity += 1
        elif action == 'remove' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart_view')
