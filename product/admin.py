# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from product.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
