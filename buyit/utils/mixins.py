from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from home.models import CustomUser
from store.models import Order


class CheckOrderTotalPrice(AccessMixin):
    
    def dispatch(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user, ordered=False)[0]
        if order.get_overall_price <= 0:
            return redirect('/')
        return super(CheckOrderTotalPrice, self).dispatch(request, *args, **kwargs)