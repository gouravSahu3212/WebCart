# -*- coding: utf-8 -*-
"""
Change subcategory of product 12.
"""

from django.conf import settings
from django.core.cache import caches
from django_extensions.management.jobs import QuarterHourlyJob
from numpy import product
from shop.models import Product
from django.core.management.base import BaseCommand, CommandError

class Job(QuarterHourlyJob):
    help = "Change subcategory of a product"

    def execute(self):
        try:
            product = Product.objects.get(id=12)
        except Product.DoesNotExist:
            raise CommandError('Product "12" does not exist')
        if product.sub_category == 'Good':
            product.sub_category = 'Bad'
        else:
            product.sub_category = 'Good'

        product.save()
        print('Successfully run this job')
        return

