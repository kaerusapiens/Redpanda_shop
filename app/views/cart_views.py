from django.views.generic import View, ListView
from app.models import Product
from collections import OrderedDict
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

#Debugのため追記
import logging
logger = logging.getLogger('project')

#カート追加
class AddToCartView(LoginRequiredMixin, View): 
    def post(self,request):
        item_pk = request.POST.get('item_pk')
        quantity = request.POST.get('quantity')
        cart = request.session.get('cart',None)
        if cart is None or len(cart) == 0:
            items=OrderedDict()
            cart = {'items':items}
        if item_pk in cart['items']:
            cart['items'][item_pk] += int(quantity)
        else:
            cart['items'][item_pk] = int(quantity)
        request.session['cart'] = cart
        return redirect('/cart/')


#カートでリストを表示する。
class CartListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'cart_view.html'
    def get_queryset(self):
        cart = self.request.session.get("cart",None)
        if cart is None or len(cart) == 0:
            return redirect("/cart/")
        self.queryset = []
        self.total = 0
        for item_pk, quantity in cart['items'].items():
            obj = Product.objects.get(pk=item_pk)
            obj.quantity = quantity
            obj.subtotal = int(obj.product_price) * quantity
            self.queryset.append(obj)
            self.total += obj.subtotal
        cart["total"] = self.total
        self.request.session["cart"] = cart
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["total"] = self.total
        except Exception as e:
            print(e)
        return context

#カートから削除
@login_required #LoginRequiredMixin のDecorator
def remove_from_cart(request,pk):
    cart = request.session.get('cart',None)
    if cart is not None:
        del cart['items'][pk]
        request.session['cart'] = cart
    return redirect('/')

#カートで数量を更新
class UpdateCartView(View):
    def post(self, request,pk):
        try:
            data = json.loads(request.body)
            quantity = data.get('quantity')
            cart = request.session.get('cart', None)
            logger.debug(f"Debug: Received cart: {cart}")
            logger.debug(f"Debug: Received cart: ",cart['items'] )
            if cart is not None and str(pk) in cart['items']:
                cart['items'][pk] = int(quantity)
                # Update the session
                request.session['cart'] = cart

                # Recalculate totals
                total = 0
                for item_pk, quantity in cart['items'].items():
                    product = Product.objects.get(pk=item_pk)
                    subtotal = int(product.product_price) * quantity
                    total += subtotal
                cart['total'] = total
                request.session['cart'] = cart
                return JsonResponse({'success': True, 'subtotal': subtotal, 'total': total})
            else:
                return JsonResponse({'success': False, 'error': 'Item not in cart or cart is empty.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})