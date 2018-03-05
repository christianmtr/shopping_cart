# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

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
