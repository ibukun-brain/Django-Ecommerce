from store.models import Order

def get_or_set_order_session(request):
    if not request.user.is_authenticated:
        request.session.set_expiry(209600)
        order_id = request.session.get('order_id', None)
        if order_id is None:
            order = Order()
            order.save()
            request.session['order_id'] = order.id
        else:
            try:
                order = Order.objects.get(id=order_id, ordered=False)
            
            except Order.DoesNotExist:
                order = Order()
                order.save()
                request.session['order_id'] = order.id    

    else:
        # order = Order.objects.get(user=request.user, ordered=False)
        order, _ = Order.objects.get_or_create(user=request.user, ordered=False)
       
    return order
