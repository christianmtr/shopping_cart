# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User)
    product = models.ManyToManyField(Product)
    is_finished = models.BooleanField(default=False, blank=False, null=False)

    def __unicode__(self):
        return self.user.username
