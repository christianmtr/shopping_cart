# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from product.models import Product


def show_products(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'base.html', {'products': products})


def one_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'one_product.html', {'product': product})
