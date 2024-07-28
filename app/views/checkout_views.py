from app.models import User, Profile, Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect


class CheckoutView(LoginRequiredMixin,View):
    def get(self, request):
        # Get user profile
        user = request.user
        profile = Profile.objects.get(user=user)

        # Get cart items
        cart = request.session.get('cart', {'items': {}, 'total': 0})
        items = []
        total = 0
        for item_pk, quantity in cart['items'].items():
            product = Product.objects.get(pk=item_pk)
            subtotal = int(product.product_price) * quantity
            items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
            total += subtotal

        # Prepare context
        context = {
            'user': user,
            'profile': profile,
            'items': items,
            'total': total,
        }
        return render(request, 'checkout.html', context)

    def post(self, request):
        # Handle form submission
        shipping_option = request.POST.get('shipping_option')
        if shipping_option:
            # Process order with the selected shipping option
            # (for simplicity, this example does not include order processing logic)
            return redirect('order_confirmation')

        # If no shipping option is selected, reload the checkout page
        return self.get(request)
    
class OrderConfirmationView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'order_confirmation.html')