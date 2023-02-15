import stripe
import json
from django.shortcuts import redirect
from ..config import STRIPE_API_KEY

class Payments:

    def session(price: str, quantity: int = 1):
        try:
            stripe.api_key = STRIPE_API_KEY

            checkout_session = stripe.checkout.Session.create(
                success_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                cancel_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                payment_method_types = ['card'],
                line_items = [
                    {
                        "price": price,
                        "quantity": quantity,
                    },
                ],
                mode = "payment"
            )
        
            return redirect(checkout_session.url)
        except Exception as e:
            return str(e)

class Product:

    def info(product_id: str):
        try:
            stripe.api_key = STRIPE_API_KEY
            
            product_info = stripe.Product.retrieve(product_id)
            info_needed = dict(), product_info['default_price']

            info_needed[0]['name'] = product_info['name']
            info_needed[0]['description'] = product_info['description']

            return info_needed
        except Exception as e:
            pass

    def price(price_id: str):
        try:
            stripe.api_key = STRIPE_API_KEY
            
            product_price = stripe.Price.retrieve(price_id)

            return product_price
        except Exception as e:
            pass