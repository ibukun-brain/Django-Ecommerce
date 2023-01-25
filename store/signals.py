import uuid
from allauth.account.signals import user_logged_in
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from store.models import Category, Product, Order, OrderItem
from home.models import CustomUser
from store.helpers import get_or_set_order_session

from buyit.utils.strings import generate_ref_no


def create_slug(model, instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = model.objects.filter(slug=slug).order_by('pk')
    exists = qs.exists()
    if exists:
        uuid_start = str(uuid.uuid1()).split("-", 1)[0] 
        new_slug = "%s-%s" %(slug, uuid_start)
        return create_slug(model, instance, new_slug=new_slug)

    return slug

@receiver(pre_save, sender=Category)
def pre_save_category_slug_reciever(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(Category, instance)
    try:
        category = Category.objects.get(pk=instance.pk)
        if instance.name != category.name:
            instance.slug = create_slug(Category, instance)
    except Category.DoesNotExist:
        pass

@receiver(pre_save, sender=Product)
def pre_save_product_slug_reciever(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(Product, instance)
    try:
        product = Product.objects.get(pk=instance.pk)
        if instance.name != product.name:
            instance.slug = create_slug(Product, instance)
    except Product.DoesNotExist:
        pass

@receiver(pre_save, sender=Order)
def post_save_generate_order_ref_no(sender,  instance, **kwargs):
    if not instance.reference_number:
        instance.reference_number = f"ORDER-{generate_ref_no()}"
        # order.save()

@receiver(user_logged_in, sender=CustomUser)
def check_logged_in_user(sender, request, **kwargs):
    # print(kwargs)
    # order = get_or_set_order_session(request)
    order = Order.objects.get(pk=request.session.get('order_id'))
    order_items = OrderItem.objects.filter(order=order)
    # color = None
    size = None
    if order_items.exists():
        for order_item in order_items:
            product = order_item.product
            # if order_item.color is not None:
            #     color = order_item.color
            if order_item.size is not None:
                size = order_item.size

            order, _ = Order.objects.get_or_create(user=request.user, ordered=False)
            order_item, created = OrderItem.objects.get_or_create(
                order=order,
                product=product,
                # color=color,
                size=size,
            )
            if not created:
                order_item.quantity += 1
                order_item.save()

    print('hello')