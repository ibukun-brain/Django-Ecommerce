from store.models import Order
def get_or_set_order_session(request):
    request.session.set_expiry(209600)
    order_id = request.session.get('order_id', None)
    order = Order()
    print(order_id)
    if order_id is None:
        order = Order()
        order.save()
        request.session['order_id'] = order.id
    # else:
    #     try:
    #         order = Order.objects.get(id=order_id, ordered=False)
            
    #     except Order.DoesNotExist:
    #         order = Order()
    #         order.save()
    #     # order = Order.save()
    #         request.session['order_id'] = order.id    

    #     if request.user.is_authenticated and order.user is None:
    #         order.user = request.user
    #         order.save()
    
    # print(order.id)
    # order = order.objects.get(id=order_id)
    # return order.filter(user=request.user)
    # queryset = order.objects.filter(user=request.user)
    return order 

    # if request.user.is_authenticated() and reques:
    # print(request.session.get('order_id'))
    # request.session.set_expiry(209600)
    # order_id = request.session.get('order_id', None)
    # if order_id is None:
    #     order = Order()
    #     order.save()
    #     request.session['order_id'] = order.id
    # else:
    #     try:
    #         order = Order.objects.select_related(
    #             'user','shipping_address',
    #             'billing_address',
    #         ).prefetch_related('orderitem_set') \
    #         .filter(id=order_id, user=request.user, ordered=False)[0]  
    #     except Order.DoesNotExist:
    #         order = Order()
    #         order.save()
    #     # order = Order.save()
    #         request.session['order_id'] = order.id

    # if request.user.is_authenticated and order.user is None:
    #     order.user = request.user
    #     order.save()
    #     print(order.user)
    #     # order = order.objects.get(id=order_id)
    #     # return order.filter(user=request.user)
    #     # queryset = order.objects.filter(user=request.user)
    # return order