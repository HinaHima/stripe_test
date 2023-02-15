from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .stripe_interaction import api_calls, parsing
from .models import Item

import stripe

@require_http_methods(["GET"])
def main_page(request):
    try:
        return render(request, 'app_itself/page.html')
    except Exception as e:
        pass

@require_http_methods(["GET"])
def buy(request, id):
    try:
        item_needed = Item.get_item_by_id(id)
        return api_calls.Payments.session(item_needed[1])
    except Exception as e:
        pass

def item(request, id):
    try:
        item_needed = Item.get_item_by_id(id)

        product_info_needed = dict()

        product_info_needed['name'] = item_needed[0]
        product_info_needed['description'] = item_needed[3]
        product_info_needed['price'] = item_needed[4]
        product_info_needed['currency'] = item_needed[5]
        product_info_needed['id'] = id
        
        return render(request, 'app_itself/purchase.html', context= product_info_needed)
        #return HttpResponse(f'{product_info}')
    except Exception as e:
        pass

"""
def item(request, id):
    try:
        item_needed = Item.get_item_by_id(id)

        product_info_needed = dict()

        product_info = api_calls.Product.info(item_needed[2])
        product_info_needed['name_and_description'] = product_info[0]

        product_info_needed['price'] = api_calls.Product.price(product_info[1])

        return render(request, 'app_itself/purchase.html', context= product_info_needed)
        #return HttpResponse(f'{product_info}')
    except Exception as e:
        pass """