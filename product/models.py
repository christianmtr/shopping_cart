# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    short_description = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    photo = models.ImageField(upload_to='product/', blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    category = models.ForeignKey(Category)
    is_active = models.BooleanField(default=True, blank=False, null=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return 'product/%s/' % self.id

    def add_to_cart(self):
        return '/add_cart/%s/' % self.id
