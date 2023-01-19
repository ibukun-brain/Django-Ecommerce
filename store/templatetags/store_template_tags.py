from django import template
from store.helpers import get_or_set_order_session

register = template.Library()

@register.filter
def order_item_count(request):
    order = get_or_set_order_session(request)
    count = order.orderitem_set.count()

    return count
    pass
