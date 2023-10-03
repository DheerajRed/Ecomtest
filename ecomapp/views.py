from django.shortcuts import render,redirect, get_object_or_404
from .models import Products, Cart
# Create your views here.
def Home(request):
    products = Products.objects.all()
    context = {
        "data":products, 
    }
    return render(request, 'index.html', context)
def CartPage(request):
    cart = Cart.objects.all()
    context = {
        'data':cart
    }
    return render(request, 'cart.html', context)

def AddtoCart(request, product_id):
    try:
        product = Products.objects.get(pk=product_id)
        cart_item = Cart(
            product_name = product.product_name,
            product_category = product.product_category,
            product_price = product.product_price
        )
        cart_item.save()
        return redirect('cart')

    except Products.DoesNotExist:
        return redirect('')

def DeleteCartItem(request, product_id ):
    cart_item = get_object_or_404(Cart, id=product_id)
    if request.method=="POST":
        cart_item.delete()
        return redirect('cart')
