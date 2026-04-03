from django.shortcuts import render,redirect
from .models import Product,Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products':products})



@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    Cart.objects.create(user=request.user, product=product)
    return redirect('cart')


@login_required
def cart_view(request):
    items = Cart.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'items': items})
# Create your views here.

from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()   
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'store/signup.html', {'form': form})


def user_page(request):
    return render(request, 'store/user.html')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(Cart, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

def show_productDetails(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/productDetails.html', {'product': product})
