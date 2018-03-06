# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Create your views here.
from cart.models import Cart
from product.models import Product


@login_required(login_url='/login/')
def add_cart(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        redirect('product/%s/' % id)
    else:
        try:
            cart = Cart.objects.get(user=request.user, is_finished=False)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user, is_finished=False)
        finally:
            cart.product.add(product)
            return redirect('/')


@login_required(login_url='/login/')
def my_cart(request):
    cart, products = None, None
    try:
        cart = Cart.objects.get(user=request.user, is_finished=False)
    except Cart.DoesNotExist:
        print("Cart empty")
    else:
        products = cart.product.all()
    finally:
        return render(request, 'my_cart.html', {'cart': cart, 'products': products})


@login_required(login_url='/login/')
def pay_cart(request):
    try:
        cart = Cart.objects.get(user=request.user, is_finished=False)
    except Cart.DoesNotExist:
        redirect("/")
    else:
        cart.is_finished = True
        cart.save()
    finally:
        return redirect("/")
