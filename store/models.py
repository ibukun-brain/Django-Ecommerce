import uuid
import auto_prefetch
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.template.defaultfilters import pluralize
from buyit.utils.models import NamedTimeBasedModel, TimeBasedModel
from buyit.utils.media import store_image_upload_path
from buyit.utils.choices import PaymentChoices
from buyit.utils.strings import generate_ref_no


# Create your models here.
class Category(NamedTimeBasedModel):
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to=store_image_upload_path, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("store:category-detail", kwargs={"slug": self.slug})
    

class Product(NamedTimeBasedModel):
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to=store_image_upload_path, blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveSmallIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    categories = models.ManyToManyField('store.Category', blank=True)
    # available_colors = models.ManyToManyField(
    #     'store.ColorVariation', blank=True,
    # )
    available_sizes = models.ManyToManyField(
        'store.SizeVariation', blank=True,
    )

    def get_absolute_url(self):
            return reverse("store:product-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.name} - ₦{self.price}"


    def image_url(self):
        if self.image:
            return self.image.url
        
        return f"{settings.STATIC_URL}/images/banners/1.jpg"
    

class SizeVariation(NamedTimeBasedModel):
    # stock = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"
    
class ColorVariation(NamedTimeBasedModel):
    # stock = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"
    


class Order(TimeBasedModel):
    user = auto_prefetch.ForeignKey(
        'home.CustomUser',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    ordered_date = models.DateTimeField(
        blank=True,
        null=True
    )
    ordered = models.BooleanField(default=False)
    address = auto_prefetch.ForeignKey(
    'home.Address',
    blank=True, 
    null=True,
    on_delete=models.SET_NULL
)
    # billing_address = auto_prefetch.ForeignKey(
    #     'home.Address',
    #     related_name='billing_address',
    #     blank=True, 
    #     null=True,
    #     on_delete=models.SET_NULL
    # )
    # shipping_address = auto_prefetch.ForeignKey(
    #     'home.Address',
    #     blank=True, 
    #     null=True,
    #     on_delete=models.SET_NULL
    # )
    reference_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return str(self.reference_number)
    
    # @property
    # # use signals to handle this better or properly
    # def reference_number(self):
    #     return f"ORDER-{generate_ref_no()}"
    
    @property
    def get_overall_price(self):
        total = 0
        for order_item in self.orderitem_set.all():
            total += order_item.get_total

        return total
    

class OrderItem(TimeBasedModel):
    product = auto_prefetch.ForeignKey(
        'store.Product',
        on_delete=models.CASCADE,
        null=True
    )
    order = auto_prefetch.ForeignKey(
        'store.Order',
        on_delete=models.CASCADE,
        null=True,
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        blank=True
    )
    # color = auto_prefetch.ForeignKey(
    #     'store.ColorVariation',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    # )
    size = auto_prefetch.ForeignKey(
        'store.SizeVariation',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

    def __str__(self):
        if self.size is not None:
            size = self.size.name
            return f"{self.product} x {self.quantity} - {size}"
        return f"{self.product} x {self.quantity}"


class Payment(TimeBasedModel):
    order = auto_prefetch.ForeignKey(
        'store.Order',
        on_delete=models.SET_NULL,
        related_name='payments',
        null=True
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentChoices.choices,
        default=PaymentChoices.PayPal    
    )
    successful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return f"{self.order} - {self.payment_method} - {self.amount}"
    

    class Meta:
        ordering = ['-created_at']