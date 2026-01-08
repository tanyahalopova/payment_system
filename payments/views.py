from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import stripe
from rest_framework.decorators import api_view

from config import settings
from payments.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
@api_view(["GET"])
def create_checkout(request, id):
    item = get_object_or_404(Item, id=id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': item.currency,
                    'unit_amount': item.get_stripe_price(),
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )
    return JsonResponse({'id': session.id})

def get_detail_item(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        "item": item,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
    }
    return render(request, "item_detail.html", context)